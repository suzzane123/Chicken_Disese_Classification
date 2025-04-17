import os
from constants import *

from dataclasses import dataclass
import os


class DataIngestionConfig:
    def __init__(self, data_ingestion_artifacts_dir, gcp_data_file_path, output_file_path, csv_data_file_path):
        self.data_ingestion_artifacts_dir = data_ingestion_artifacts_dir
        self.gcp_data_file_path = gcp_data_file_path
        self.output_file_path = output_file_path
        self.csv_data_file_path = csv_data_file_path
        self.connection_string = AZURE_STORAGE_CONNECTION_STRING
        self.container_name = AZURE_CONTAINER_NAME


@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.data_transformation_artifacts_dir: str = os.path.join(ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)

        self.labels_to_ids_path: str = os.path.join(self.data_transformation_artifacts_dir, LABELS_TO_IDS_FILE_NAME)
        self.ids_to_labels_path: str = os.path.join(self.data_transformation_artifacts_dir, IDS_TO_LABELS_FILE_NAME)
        self.df_train_path: str = os.path.join(self.data_transformation_artifacts_dir, DF_TRAIN_FILE_NAME)
        self.df_val_path: str = os.path.join(self.data_transformation_artifacts_dir, DF_VAL_FILE_NAME)
        self.df_test_path: str = os.path.join(self.data_transformation_artifacts_dir, DF_TEST_FILE_NAME)
        self.unique_labels_path: str = os.path.join(self.data_transformation_artifacts_dir, UNIQUE_LABELS_FILE_NAME)