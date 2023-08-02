import os
import urllib.request as request
import zipfile
from cassava_disease_project import logger
from cassava_disease_project.utils.common import get_size
from cassava_disease_project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def extract_zip_folder(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.source_dir, "r") as zip_ref:
            zip_ref.extractall(unzip_path)

    def extract_zip_train(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.train_dir, "r") as zip_ref:
            zip_ref.extractall(unzip_path)

    def extract_zip_test(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.test_dir, "r") as zip_ref:
            zip_ref.extractall(unzip_path)