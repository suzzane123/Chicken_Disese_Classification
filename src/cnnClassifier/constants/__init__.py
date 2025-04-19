import os
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts",TIMESTAMP)
LOGS_DIR = "logs"
LOGS_FILE_NAME = "ner.log"


AZURE_STORAGE_CONNECTION_STRING = ""
AZURE_CONTAINER_NAME = ""
BUCKET_NAME = ""
GCP_DATA_FILE_NAME = "" # This is the zip file name
CSV_FILE_NAME = "" # This is the csv file name 


#Data Transformation 

DATA_TRANSFORMATION_ARTIFACTS_DIR = "DataTransformationArtifacts"
LABELS_TO_IDS_FILE_NAME = "labels_to_ids.pkl"
IDS_TO_LABELS_FILE_NAME = "ids_to_labels.pkl"
DF_TRAIN_FILE_NAME = "df_train.pkl"
DF_VAL_FILE_NAME = "df_val.pkl"
DF_TEST_FILE_NAME = "df_test.pkl"
UNIQUE_LABELS_FILE_NAME = "unique_labels.pkl"