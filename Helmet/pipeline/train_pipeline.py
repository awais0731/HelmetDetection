from Helmet.entity.config_entity import DataIngestionConfig
from Helmet.entity.artifacts_entity import DataIngestionArtifacts
from Helmet.components.data_ingestion import DataIngestion
from Helmet.configuration.s3_operations import S3Operation
from Helmet.logger import logging
from Helmet.exception import HelmetException
import os, sys

class TrainPipeline:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()


    
    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")

        try:
            logging.info("Getting the data from S3 bucket")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config,
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train, test and valid from s3")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact

        except Exception as e:
            raise HelmetException(e, sys) from e
        


    
    def run_pipeline(self) -> None:

        try:

            data_ingestion_artifact: DataIngestionArtifacts = self.start_data_ingestion()

            
            
        except Exception as e:
            raise HelmetException(e, sys)

