import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.pipelines.test_model_pipeline import Test_model_pipline

data='mushrooms.csv'

if __name__=='__main__':
    Test_model_pipline().run_test_pipeline(data ,"class")
    