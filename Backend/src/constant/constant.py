

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression ,LinearRegression
from sklearn.tree import DecisionTreeClassifier ,DecisionTreeRegressor
from sklearn.svm import SVC 
from sklearn.ensemble import RandomForestClassifier ,RandomForestRegressor ,GradientBoostingClassifier,GradientBoostingRegressor 
from xgboost import XGBClassifier ,XGBRFRegressor


param_grid_all_Regressor = {
    # 'SLR': {
    #     'fit_intercept': [True, False],
    #     # 'normalize' deprecated, usually not used anymore
    # },
    'Decision_Tree': {
        'max_depth': [None, 5, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': [None, 'auto', 'sqrt']
    },
    'GradientBoosting': {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.1, 0.2],
        'max_depth': [3, 5, 10],
        'subsample': [0.6, 0.8, 1.0],
        'min_samples_split': [2, 5, 10]
    },
    'XGBRegressor': {
        'n_estimators': [100, 200,],
        'learning_rate': [0.01, 0.1, 0.2],
        'max_depth': [3, 5, 10],
        'reg_alpha': [0, 0.1, 1],
        'reg_lambda': [1, 1.5, 2]
    },
    'RandomForest': {
        'n_estimators': [100, 200, 300],
        'max_depth': [ 5, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['auto', 'sqrt', 'log2'],
        'bootstrap': [True, False]
    },
}


param_grid_all_classification = {
    'LogisticRegression': {
        'penalty': ['l2', 'none', 'l1', 'elasticnet'],
        'C': [0.01, 0.1, 1, 10, 100],
        'max_iter': [100, 200]
    },
    'Decision_Tree': {
        'max_depth': [None, 5, 10, 20],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2, 4],
        'max_features': [None, 'auto', 'sqrt', 'log2']
    },
    'RandomForest': {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 5, 10, 20],
        'min_samples_split': [2, 5, 10],
        'max_features': ['auto', 'sqrt', 'log2'],
        'bootstrap': [True, False]
    },
    'GradientBoosting': {
        'n_estimators': [100, 200],
        'learning_rate': [0.01, 0.1],
        'max_depth': [3, 5, 10],

    },
    'XGBClassifier': {
        'n_estimators': [100, 200],
        'learning_rate': [0.01, 0.1],
        'max_depth': [3, 5, 10],
        'reg_alpha': [ 0.1, 1],
        'reg_lambda': [1, 1.5, 2]
    }
}















modelRegressor={
    # 'SLR':LinearRegression(),
    'Decision_Tree':DecisionTreeRegressor(),
    'RandomForest':RandomForestRegressor(),
    'GradientBoosting':GradientBoostingRegressor(),
    'XGBRegressor':XGBRFRegressor(),
}


modelClassifier={
    # 'LogisticRegression':LogisticRegression(), 
    'Decision_Tree':DecisionTreeClassifier(),
    'RandomForest':RandomForestClassifier(),
    'GradientBoosting':GradientBoostingClassifier(),
    'XGBClassifier':XGBClassifier(),}