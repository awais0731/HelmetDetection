
from Helmet.configuration.s3_operations import S3Operation
from Helmet.constant.training_pipeline import *
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    def __init__(self):
        
        self.data_folder:str = Data_FOLDER
        self.artifact_dir:str = os.path.join(ARTIFACT_DIR, TIMESTAMP)

        self.data_path:str = os.path.join(self.artifact_dir, "data_ingestion", self.data_folder)

        self.train_data_path:str = os.path.join(self.data_path, "train")
        self.test_data_path:str = os.path.join(self.data_path, "test")
        self.valid_data_path:str = os.path.join(self.data_path, "test")