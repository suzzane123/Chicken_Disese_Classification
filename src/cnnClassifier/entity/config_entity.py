import os
from constants import AZURE_STORAGE_CONNECTION_STRING, AZURE_CONTAINER_NAME

class DataIngestionConfig:
    def __init__(self, data_ingestion_artifacts_dir, gcp_data_file_path, output_file_path, csv_data_file_path):
        self.data_ingestion_artifacts_dir = data_ingestion_artifacts_dir
        self.gcp_data_file_path = gcp_data_file_path
        self.output_file_path = output_file_path
        self.csv_data_file_path = csv_data_file_path
        self.connection_string = AZURE_STORAGE_CONNECTION_STRING
        self.container_name = AZURE_CONTAINER_NAME