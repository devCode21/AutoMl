# acces the store model then if you want form data extract the import features then ask for ii else upload csv file of test  data 
# formdata and csv data 

# model config , model , formdata , csv data preporcsising value return 
import joblib
from dataclasses import dataclass
from src.logger import logging
import numpy as np
import pandas as pd
import os ,sys  
from src.constant.lib_constant import CustomException


def appy_preprocess_techniques(X_test):
      try: 
        preprocess=joblib.load('artifacts/preprocss.pkl')
        if(len(preprocess["numericals_cols_before_vif"])>0):
               X_test_numeric=X_test[preprocess['numericals_cols_before_vif']]
               X_test_transform_numeric=preprocess["numeric_pipline"].transform(X_test_numeric)
        if len(list(preprocess['categorical_cols_before_ohe']))>0:
                X_test_categorical=X_test[preprocess['categorical_cols_before_ohe']]
                X_test_transform_cat=preprocess["categorical_Pipeline"].transform(X_test_categorical)
                columns=preprocess["numericals_cols_before_vif"]+preprocess["categorical_cols"]
                if(len(preprocess["numericals_cols_before_vif"])>0):
                    X_test_transformed=pd.DataFrame(np.hstack((X_test_transform_numeric,X_test_transform_cat)),columns=columns)
                else:
                      X_test_transformed=pd.DataFrame(X_test_transform_cat,columns=list(preprocess["categorical_cols"]))
                    
                      
        else:
               columns=preprocess["numericals_cols_before_vif"]
               X_test_transformed=pd.DataFrame(X_test_transform_numeric,columns=columns)
              
        logging.info(f"Transformed test data shape: {X_test_transformed.shape}")
        np.save('x_test',X_test_transformed[preprocess['feature_name']]) 
        X_test_transformed[preprocess['feature_name']].to_csv("transformed_test.csv", index=False)
        return X_test_transformed
      except Exception as e:
             raise CustomException(e,sys)


class test_pipelineConfig:
    model="artifacts/model/model.pkl"
    form_features="features.npy"
    artifacts="artifacts"
    model_predicts_csv_file="artifacts/model_prediction/model_predict.csv"
    preprocessor="artifacts/preprocss.pkl"

class Test_model_pipline:
    def __init__(self):
        self.config=test_pipelineConfig()
        self.model=joblib.load(self.config.model)
        self.preprocess=joblib.load(self.config.preprocessor)
    
    def form_test_model_pipline(self,data):
       try: 
        raw_features=np.load(os.path.join(self.config.artifacts ,self.config.form_features),allow_pickle=True).item()
        form_features=raw_features["form_features"]
        if(set(data.keys()) != set(form_features)):
             return "features are missing"
        features_not_in_form=raw_features["values_of_feature_not_in_form"]
        features=data|features_not_in_form
        X_predict_data=pd.DataFrame([features])
        X_predict_data_transformed=appy_preprocess_techniques(X_predict_data )
        y_pred=self.model.predict(X_predict_data_transformed)
        preprocess=joblib.load('artifacts/preprocss.pkl')
        if(preprocess.get('en')):
             y_pred= preprocess['le'].inverse_transform(y_pred)
        
        logging.info(y_pred)
        
        return y_pred
       except Exception as e:
            raise CustomException(e,sys)
    
    def csv_data_test_model_pipline(self , csv_data):
       try:
         data=pd.read_csv(csv_data)
         features_req=list(self.preprocess["features_before_transfromation"].keys())
        
         
         if set(features_req).issubset(set(data.columns)):
                  data[features_req]
         else:
                  feature_not_in=[]
                  for i in list(data.columns):
                        if i not in features_req:
                              feature_not_in.append(i)
                  logging.info(feature_not_in)
                  return 1
                  
         X_predict_data_transformed=appy_preprocess_techniques(data)
         logging.info(type(X_predict_data_transformed),X_predict_data_transformed , X_predict_data_transformed.shape)
         if(self.preprocess.get('le')):
               data['TARGET']= self.preprocess['le'].inverse_transform(self.model.predict(X_predict_data_transformed))
         
         data['TARGET']=self.model.predict(X_predict_data_transformed)
        #  store final results
         data.to_csv(os.path.join(self.config.artifacts ,'pred' ,'predicted_data.csv'),index=False)

       except Exception as e:
            raise CustomException(e,sys)
         
    def run_test_pipeline(self,data ,type_of_data):
       
       try:  
        return self.form_test_model_pipline(data) if type(data) == dict else self.csv_data_test_model_pipline(data)
       except Exception as e:
             raise CustomException(e ,sys)



         
   
    
    


        
