from dataclasses import dataclass
class DataIngestionArtifacts:
    def __init__(self, zip_data_file_path, csv_data_file_path):
        self.zip_data_file_path = zip_data_file_path
        self.csv_data_file_path = csv_data_file_path

    def __repr__(self):
        return f"DataIngestionArtifacts(zip_data_file_path={self.zip_data_file_path},csv_data_file_path={self.csv_data_file_path})"




#Data Transformation Artifacts

@dataclass
class DataTransformationArtifacts:
    labels_to_ids_path: str
    ids_to_labels_path: str
    df_train_path: str
    df_val_path: str
    df_test_path: str
    unique_labels_path: str

