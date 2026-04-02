import os
import sys
import dill
import yaml
import base64
from src.logger import logging
from src.exception import CustomException


def save_object(file_path: str, obj: object) -> None:
    logging.info(f"Saving object to {file_path}")
    
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Object saved successfully to {file_path}")
        
    except Exception as e:
        logging.error(f"Error occurred while saving object to {file_path}: {e}")
        raise CustomException(e, sys) from e
    
    
def load_object(file_path: str) -> object:
    logging.info(f"Loading object from {file_path}")
    
    try:
        with open(file_path, 'rb') as file_obj:
            obj = dill.load(file_obj)
        logging.info(f"Object loaded successfully from {file_path}")
        return obj
        
    except Exception as e:
        logging.error(f"Error occurred while loading object from {file_path}: {e}")
        raise CustomException(e, sys) from e
    
    
def image_to_base64(image_path: str) -> str:
    logging.info(f"Converting image at {image_path} to base64 string")
    
    try:
        with open(image_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        logging.info(f"Image at {image_path} converted to base64 string successfully")
        return encoded_string
        
    except Exception as e:
        logging.error(f"Error occurred while converting image at {image_path} to base64 string: {e}")
        raise CustomException(e, sys) from e
    
    
def read_yaml_file(file_path: str) -> dict:
    logging.info(f"Reading YAML file from {file_path}")
    
    try:
        with open(file_path, 'rb') as yaml_file:
            data = yaml.safe_load(yaml_file)
        logging.info(f"YAML file at {file_path} read successfully")
       
    except Exception as e:
        logging.error(f"Error occurred while reading YAML file from {file_path}: {e}")
        raise CustomException(e, sys) from e

