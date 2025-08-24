import os 
import sys 
from dataclasses import dataclass
import pandas as pd
import numpy as np
from src.logger import logging
from src.utils.ongoin import ongoing_add
from src.exception import CustomException

from sklearn.impute import SimpleImputer
import joblib
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder ,StandardScaler
from sklearn.pipeline  import Pipeline
from statsmodels.stats.outliers_influence import variance_inflation_factor
from imblearn.pipeline import Pipeline as PipLine2
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from src.utils.ongoin import ongoing_add
from sklearn.preprocessing import LabelEncoder
