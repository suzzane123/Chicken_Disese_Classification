import os
import sys
import torch
from torch.optim import SGD
from torch.utils.data import DataLoader
from tqdm import tqdm 
from transformers import BertTokenizerFast
from model.bert import BertModel
from cnnClassifier.constants import *

class DataSequence(torch.utils.data.DataSet):
    def __init__(self, df, tokenizer, labels_to_ids):
        lb = [i.split() for i in df["labels"].values.tolist()]
        txt = df["text"].values.tolist()
        self.texts = [
            tokenizer(str(i), padding = "max_length", max_length=512, truncation =True, return_tensors="pt")
            for i in txt
        ]
        self.labels = [
            self.align_label(i, j,tokenizer, labels_to_ids) for i, j in zip(txt, lb)
        ]

    def __len__(self) -> int:
        return (self.labels)
    
    def get_batch_data(self, idx):
        return self.texts[idx]
    def get_batch_label(self, idx):
        return  torch.LongTensor(self.labels[idx])
    
    def __getitem__(self, idx):
        batch_data = self.get_batch_data(idx)
        batch_lables = self.get_batch_label(idx)

    def align_label(self, texts: str, labels: str, tokenizer: dict, labels_to_ids: dict) -> list:
        try:
            logging.info("Entered the align_label method of DataSequence Class ")
            label_all_tokens = False
            tokenized_inputs = tokenizer(texts, padding="max_length", max_length=512, truncation= True)

            word_ids = tokenized_inputs.word_ids()

            previous_word_idx = None
            label_ids = []

            for word_idx in word_ids:
                if word_idx is None:
                    label_ids.append(-100)
                elif word_idx != previous_word_idx:
                    try:
                        label_ids.append(labels_to_ids[labels[word_idx]])
                    except:
                        label_ids.append(-100)
                else:
                    try:
                        label_ids.append(
                            labels_to_ids[labels[word_idx]]
                            if label_all_tokens
                            else -100
                        )
                    except: 
                        label_ids.append(-100)
                previous_word_idx = word_idx
            logging.info("Exited the align_label method of DataSequence Class ")
            return labels_to_ids
        except Exception as e:
            raise NerException(e, sys) from e
        

class ModelTraining:
    def __init__(
            self, 
            model_training_config: ModelTrainingConfig, 
            data_transformation_artifacts: DataTransformationArtifacts,

    ) -> None:
        self.model_training_config = model_training_config
        self.data_tranformation_artifacts = data_transformation_artifacts
        self.utils = MainUtils()
        self.azure_blob = AzureBlobSyncer()

    def initiate_model_training(self) -> ModelTrainingArtifacts:
        try:
            logging.info("Entered the initiate_model_training method of Model Training class ")
            os.makedirs(
                self.model_training_config.model_training_artifacts_dir , exist_ok=True
            )
            logging.info(f"Created {os.path.basename(self.model_training_config.model_training_artifacts_dir)} directory")

            tokenizer = BertTokenizerFast.from_pretrained("bert-base-cased")
            logging.info("Downloaded tokenizer")

            learning_rate = LEARNING_RATE
            epoch = EPOCHS
            batch_size = BATCH_SIZE

            unique_labels = self.utils.load_pickle_file(
                filepath = self.data_tranformation_artifacts.unique_labels_path
            )
            logging.info(f"Loaded {os.path.basename(self.data_tranformation_artifacts.unique_labels_path)} picke file from artifacts directory")

            df_train = self.utils.load_pickle_file(
                filepath = self.data_tranformation_artifacts.df_train_path
            )
            logging.info(f"Loaded {os.path.basename(self.data_tranformation_artifacts.df_train_path)} pickle file artifacts directory")
            
            df_val = self.utils.load_pickle_file(
                filepath = self.data_tranformation_artifacts.df_val_path
            )
            logging.info(f"Loadd {os.path.basename(self.data_tranformation_artifacts.df_val_path)} picke file artifacts directory")

            labels_to_ids = self.utils.load_pickle_file(
                filepath = self.data_tranformation_artifacts.labels_to_ids_path
            )
            logging.info(f"Loaded {os.path.basename(self.data_tranformation_artifacts.labels_to_ids_path)} pickle file artifacts directory")