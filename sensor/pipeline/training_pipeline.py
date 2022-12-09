from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.exception import SensorException
import sys,os
from sensor.logger import logging
from sensor.components.data_ingestion import DataIngestion

class TrainPipeline:
    
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        
        #self.training_pipeline_config=training_pipeline_config
        
     # this is my first data ingestion component   
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            # first we create a data ingestion configuration
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            # then we create a object of component. then we pass the configuration
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            # and then finally we started the ingestion and then we get the output data_ingestion_artifact 
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e,sys)
