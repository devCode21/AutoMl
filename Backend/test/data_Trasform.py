from src.components.dataTranformation import get_best_features
from src.constant.lib_constant import os ,sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__=='__main__':
    get_best_features().run()