# extract import featurs 
from src.components.dataIngestion import DataIngestion
from src.components.dataTranformation import X_trainTransform
from src.components.model import Model
from dataclasses import dataclass


data='abalone.csv'


class Train_model_pipline:
    def __init__(self):
        self.DatInges=DataIngestion()
        self.dataTransform=X_trainTransform()
        self.model=Model()
    
    def runTrain_piline(self ,data,target , drop_cols ,type_model):
        self.DatInges.store_data(data)
        self.dataTransform.run_DataTransformation(data ,target,drop_cols)
        self.model.run_Model(type_model)
        

