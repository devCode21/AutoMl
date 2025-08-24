import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.components.model import Model
from src.components.dataIngestion import DataIngestion
from src.components.dataTranformation import X_trainTransform

data='mushrooms.csv'

if __name__=='__main__':
    DataIngestion().store_data(data)
    X_trainTransform().run_DataTransformation(data,"class" )

    Model().run_Model('')
