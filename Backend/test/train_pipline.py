import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Backend.src.pipelines.train_model_pipline import Train_model_pipline

data='real_estate_dataset.csv'

if __name__=='__main__':
    Train_model_pipline().runTrain_piline(data ,"Price", "ID" ,"Regressor")
    