from cassava_disease_project.config.configuration import ConfigurationManager
from cassava_disease_project.components.data_ingestion import DataIngestion
from cassava_disease_project import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.extract_zip_folder()
        data_ingestion.extract_zip_train()
        data_ingestion.extract_zip_test()

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e 
        
