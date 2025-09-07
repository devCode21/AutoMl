
import os 
import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.components.dataIngestion import DataIngestion

data='real_estate_dataset.csv'

if __name__=='__main__':
    DataIngestion().store_data(data,'Train_data')
