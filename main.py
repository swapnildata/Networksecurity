
import sys
from Networksecurity.componenets.data_ingestion import DataIngestion
from Networksecurity.componenets.data_validation import DataValidation
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logging
from Networksecurity.constants.training_pipeline import SCHEMA_FILE_PATH
from Networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from Networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info('Initiated data ingestion')
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info('Data ingestion completed')
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info('Initiated data validation')
        data_validation_artifact=data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info('Completed data validation.')
    except Exception as e:
            raise NetworkSecurityException(e,sys)
