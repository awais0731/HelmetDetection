
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



@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.ROOT_DIR: str = os.path.join(ARTIFACT_DIR, TIMESTAMP, DATA_INGESTION_ARTIFACTS_DIR, Data_FOLDER)
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(ARTIFACT_DIR, TIMESTAMP,DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.TRAIN_TRANSFORM_DATA_ARTIFACT_DIR = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR,DATA_TRANSFORMATION_TRAIN_DIR)
        self.TEST_TRANSFORM_DATA_ARTIFACT_DIR = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR,DATA_TRANSFORMATION_TEST_DIR)
        self.TRAIN_TRANSFORM_OBJECT_FILE_PATH = os.path.join(self.TRAIN_TRANSFORM_DATA_ARTIFACT_DIR,
                                                                DATA_TRANSFORMATION_TRAIN_FILE_NAME)
        self.TEST_TRANSFORM_OBJECT_FILE_PATH = os.path.join(self.TEST_TRANSFORM_DATA_ARTIFACT_DIR,
                                                                DATA_TRANSFORMATION_TEST_FILE_NAME)
        
        self.TRAIN_SPLIT = DATA_TRANSFORMATION_TRAIN_SPLIT
        self.TEST_SPLIT = DATA_TRANSFORMATION_TEST_SPLIT
        
