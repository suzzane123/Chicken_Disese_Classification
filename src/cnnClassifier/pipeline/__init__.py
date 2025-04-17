from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.configuration.azure_blob import AzureBlobSyncer

from cnnClassifier.components.data_ingestion import DataIngestion

def main():
    config = DataIngestionConfig(
        data_ingestion_artifacts_dir="",
        gcp_data_file_path="",
        output_file_path="", 
        csv_data_file_path=""

    )
    #Step -2 Azure blob syncer
    azure_blob_syncer = AzureBlobSyncer(config)
    #Step-3 DataIngestion
    data_ingestion = DataIngestion(config, azure_blob_syncer)
    #Step-4 : Initiate DataIngestion
    data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

    print(data_ingestion_artifacts)