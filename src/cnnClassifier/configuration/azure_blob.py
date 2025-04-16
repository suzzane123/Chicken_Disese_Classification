from azure.storage.blob import BlobServiceClient
from config_entity import DataIngestionConfig
import logging

class AzureBlobSyncer: 
    def __init__(self, config: DataIngestionConfig):
        self.blob_service_client = BlobServiceClient.from_connection_string(config.connection_string)
        self.container_client = self.blob_service_client.get_container_client(config.container_name)

    def upload_file(self, artifact_path:str, artifact_name: str):
        blob_client = self.container_client.get_blob_client(artifact_name)
        with open(artifact_path, "rb") as data:
            blob_client.upload_blob(data)
        logging.info(f"Uploaded {artifact_name} to azure Blob Storage")


    def download_file(self, artifact_path: str, artifact_name: str):
        blob_client = self.container_client.get_blob_client(artifact_name)
        with open(artifact_path, "wb") as data:
            data.write(blob_client.download_blob().readall())
        
        logging.info(f"Downloaded {artifact_name} from Azure Blob Storage")
