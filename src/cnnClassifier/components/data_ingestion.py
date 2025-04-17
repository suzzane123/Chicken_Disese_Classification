import os
import sys
from zipfile import ZipFile
from cnnClassifier.configuration.azure_blob import AzureBlobSyncer

from constants import BUCKET_NAME, GCP_DATA_FILE_NAME, CSV_FILE_NAME
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.entity.artifact_entity import DataIngestionArtifacts


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig, azure_blob_syncer: AzureBlobSyncer) -> None:
        self.data_ingestion_config = data_ingestion_config
        self.azure_blob_syncer = azure_blob_syncer
    
    def extract_data(self, input_file_path:str, output_file_path: str) -> None:
        logging.info("Entered the extract_data method of dataIngestion class")
        try:
            with ZipFile(input_file_path, "r") as zObject:
                zObject.extractall(path=output_file_path)
            logging.info("Exited the extract_data method")
        except Exception as e:
            raise NerException(e, sys) from e
    
    def initiate_data_ingestion(self)->DataIngestionArtifacts:
        logging.info("Entered the initiate_data_ingestion method of data ingestion class")
        try:
            os.makedirs(self.data_ingestion_config.data_ingestion_artifacts_dir, exist_ok=True)
            logging.info(f"Created {os.path.basename(self.data_ingestion_config.data_ingestion_artifacts_dir)} directory.")
            self.azure_blob_syncer.download_file(
                artifact_path= self.data_ingestion_config.gcp_data_file_path,
                artifact_name= GCP_DATA_FILE_NAME
            )
            logging.info(f"Got the file from Azure Blob Storage. FileName - {os.path.basename(self.data_ingestion_config.gcp_data_file_path)}")

            self.extract_data(
                input_file_path=self.data_ingestion_config.gcp_data_file_path,
                output_file_path=self.data_ingestion_config.output_file_path
            )
            logging.info(f"Extracted the data from zip file")


            data_ingestion_artifact =  DataIngestionArtifacts(
                zip_data_file_path = self.data_ingestion_config.gcp_data_file_path,
                csv_data_file_path = os.path.join(self.data_ingestion_config.output_file_path, CSV_FILE_NAME)
            )
            logging.info("Exited the initiate_data_ingestion method of data ingestion class")

            return data_ingestion_artifact
        except Exception as e:
            raise NerException(e, sys) from e