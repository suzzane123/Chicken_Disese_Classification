import os
import sys
import numpy as np
import pandas as pd
from pandas import DataFrame

from cnnClassifier.entity.artifact_entity import (DataIngestionArtifacts, DataTransformationArtifacts,)
from cnnClassifier.configuration.azure_blob import AzureBlobSyncer
from cnnClassifier.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig, data_ingestion_artifacts: DataIngestionArtifacts, azure_blob_syncer:AzureBlobSyncer) -> None:
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifacts = data_ingestion_artifacts
        self.azure_blob_syncer = azure_blob_syncer
    
    def splitting_data(self, df: DataFrame) -> dict:
        logging.info("Entered the splitting_data method of Data Transformation class")
        try:
            df = df[0:1000]
            labels = [i.split() for i in df["labels"].values.tolist()]
            unique_labels = set()

            for lb in labels:
                [unique_labels.add(i) for i in lb if  i not in unique_labels]

            labels_to_ids = {k:v for v, k in enumerate(unique_labels)}
            ids_to_labels = {v:k for v, k in enumerate(unique_labels)}

            df_train, df_val, df_test = np.split(
                df.sample(frac=1, random_state=42),
                [int(0.8*len(df)), int(0.9 *len(df))],
            )
            logging.info("Exited the splitting_data method of Data Transformation Class")

            return (labels_to_ids, ids_to_labels, df_train, df_test, df_val, unique_labels)
        except Exception as e:
            raise NerException(e, sys) from e
