from cassava_disease_project import logger
from cassava_disease_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cassava_disease_project.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cassava_disease_project.pipeline.stage_03_training import ModelTrainingPipeline
from cassava_disease_project.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception
    raise e 


STAGE_NAME = "Prepare base model"
try:
    logger.info(f"****************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
if __name__ == "__main__":
    try:
        logger.info(f"********************************")
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Evaluation stage"
if __name__ == '__main__':
    try:
        logger.info(f"********************************")
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e 