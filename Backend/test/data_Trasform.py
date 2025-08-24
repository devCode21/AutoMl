from src.components.dataTranformation import X_trainTransform
from src.constant.lib_constant import os ,sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
data='mushrooms.csv'
if __name__=='__main__':
    X_trainTransform().run_DataTransformation(data ,'class')