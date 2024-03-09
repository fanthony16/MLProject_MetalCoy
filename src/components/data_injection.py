import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataInjectionConfig:
    train_data_path: str = os.path.join("artifact","train.csv")
    test_data_path: str = os.path.join("artifact","test.csv")
    raw_data_path: str = os.path.join("artifact","data.csv")
    
class DataInjection:
    def __init__(self):
        self.injection_config = DataInjectionConfig()
    def read_data(self):
        logging.info("Reading Dataset from file path")
        try:
            
            df = pd.read_csv("notebook\data\MetalCoy_Dataset.csv")
            logging.info("Dataset read was successful")
            os.makedirs(os.path.dirname(self.injection_config.test_data_path),exist_ok=True)
            df.to_csv(self.injection_config.raw_data_path,index=False, header=True)
            
            logging.info("Train test split initiated")
            train_set, test_set= train_test_split(df, test_size=0.2, random_state= 42)
            
            train_set.to_csv(self.injection_config.train_data_path,index=False, header=True)
            test_set.to_csv(self.injection_config.test_data_path, index=False, header=True)

            logging.info("Data Injection completed")
            return(
                self.injection_config.train_data_path, self.injection_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
if __name__ == "__main__":
    obj = DataInjection()
    obj.read_data()
    
            
            
            
        
        
        