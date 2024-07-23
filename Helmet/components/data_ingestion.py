from Helmet.entity.config_entity import DataIngestionConfig
from Helmet.entity.artifacts_entity import DataIngestionArtifacts
from Helmet.configuration.s3_operations import S3Operation
from Helmet.exception import HelmetException
from Helmet.logger import logging
import sys

class DataIngestion:


    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

        self.local = S3Operation()

    
    def get_data_from_local(self) -> None:
        try:
            logging.info("Entered the get_data_from_local method of Data ingestion class")

            self.local.syn_from_local(
                src_folder="D:\DataSets\Bike Data",
                dest_folder=self.data_ingestion_config.data_path
            )

            logging.info("Exited the get_data_from_s3 method of Data ingestion class")

        except Exception as e:
            raise HelmetException(e, sys)
        

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the initiate_data_ingestion method of Data ingestion class")

        try:
            self.get_data_from_local()

            data_ingestion_artifact: DataIngestionArtifacts = DataIngestionArtifacts(
                train_file_path = self.data_ingestion_config.train_data_path,
                test_file_path = self.data_ingestion_config.test_data_path,
                valid_file_path = self.data_ingestion_config.valid_data_path
            )

            logging.info("Exited the initiate_data_ingestion method of Data ingestion class")

            return data_ingestion_artifact

        except Exception as e:
            raise HelmetException(e, sys)