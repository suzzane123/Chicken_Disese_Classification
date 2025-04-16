class DataIngestionArtifacts:
    def __init__(self, zip_data_file_path, csv_data_file_path):
        self.zip_data_file_path = zip_data_file_path
        self.csv_data_file_path = csv_data_file_path

    def __repr__(self):
        return f"DataIngestionArtifacts(zip_data_file_path={self.zip_data_file_path},csv_data_file_path={self.csv_data_file_path})"