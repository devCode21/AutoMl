import os
import sys 
import json
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score ,r2_score , mean_absolute_percentage_error
import joblib
from sklearn.metrics import classification_report , mean_absolute_error, mean_squared_error
import numpy as np
from src.constant.constant import param_grid_all_classification ,param_grid_all_Regressor ,modelClassifier,modelRegressor
from src.utils.ongoin import ongoing_add
from src.exception import CustomException

# key issuse  mishandling way of sending report ,custException ,form_features_for_LR_andSlr
# tuning time is very providing best_model without tuned model_to download 

@dataclass
class ModelConfig:
    artifacts='artifacts'
    model_dir='model'
    model_path='model.pkl'
    X_train='X_train.npy'
    X_test='X_test.npy'
    model_Reg=modelRegressor
    modelClassifier=modelClassifier
    report='artifacts/reports/model_report.json'
    preprocess="artifacts/preprocss.pkl"
    hypertuned_model_report="artifacts/reports/hypertuned_model_report.json"



def extract_features_form_data(preprocess ,best_model):
      try: 
         features=best_model.feature_importances_
         features_names={}
         
         features_mean=preprocess['features_before_transfromation']
         logging.info(features_mean)
         for i in range(0, len(features)):
              features_names[preprocess["feature_name"][i]]=features[i]

         sorted_feature=sorted(features_names ,key=features_names.get, reverse=True) 
         form_feature=sorted_feature[:10]
         values_of_feature_not_in_form={}
         for key ,value in preprocess['features_before_transfromation'].items():
              if key not in form_feature:
                   values_of_feature_not_in_form[key]=value
         
         np.save("artifacts/features.npy" ,{"form_features":form_feature , "values_of_feature_not_in_form":values_of_feature_not_in_form})
      except Exception as e:
           raise CustomException(e,sys)
#choose d/f models right on the basis or type of data we would acctualllu use the models 
# train the all model or selected models ok /tune bet model using hyperparamenter
# will provide best model for download
class Model:
    def __init__(self):
        self.config=ModelConfig() 
        self.X_train=pd.DataFrame()
        self.Y_train=pd.Series()
        self.X_test=pd.DataFrame()
        self.Y_test=pd.Series()
        self.type_of_model=""
        self.model_path=os.path.join(self.config.artifacts , self.config.model_dir , self.config.model_path)
    
    
    def initialize_the_values(self, type_of_model):
         try:
               train_data=np.load(os.path.join(self.config.artifacts,self.config.X_train), allow_pickle=True)
               test_data=np.load(os.path.join(self.config.artifacts,self.config.X_test), allow_pickle=True)
               self.X_train= train_data.item()['X_train']
               self.Y_train= train_data.item()['Y_train']
               self.X_test= test_data.item()['X_test']
               self.Y_test= test_data.item()['Y_test']    
               self.type_of_model=type_of_model
               logging.info(f"Training data shape: {self.X_train.shape}, Test data shape: {self.X_test.shape}")      
               logging.info(f"Training labels shape: {self.Y_train.shape}, Test labels shape: {self.Y_test.shape}")
         except Exception as e:
              raise CustomException(e,sys)

    def  train_model_classifier(self):
        try: 
          logging.info("Training classification models...")
          ongoing_add("Training classification models...")
          model_type=self.config.modelClassifier
          report_to_send_frontend={}
          report={}
          for (model_key,model) in model_type.items():
               model.fit(self.X_train, self.Y_train)
               y_pred=model.predict(self.X_test)
               accuracy= accuracy_score(y_pred,self.Y_test)

               clf=classification_report(self.Y_test ,y_pred, output_dict=True)
               report_to_send_frontend[model_key ]=clf
               report[model_key]=accuracy 
             
          with open('artifacts/reports/report_download', 'w') as file:
              json.dump(report_to_send_frontend, file)
          
          with open(self.config.report, 'w') as file:
              json.dump(report, file)
          ongoing_add("Training regression models completed")

          ongoing_add("Training classification models completed")
          return report
        except Exception as e:
              raise CustomException(e,sys)

   
               
    def train_model_regressor(self ):
        try:  
          ongoing_add
          logging.info("Training regression models...")
          model_type=self.config.model_Reg
          report={}
          report_to_send_frontend={}
          for (model_key,model) in model_type.items():
               model.fit(self.X_train,self.Y_train)
               y_pred=model.predict(self.X_test)
               r2_value=r2_score(self.Y_test,y_pred)
               mae=mean_absolute_percentage_error(self.Y_test,y_pred)
               clf={
                    "MAE":mean_absolute_error,
                     "varaince_explained":r2_value,
                     "MSe":mean_squared_error(self.Y_test ,y_pred )
               }
               report_to_send_frontend[model_key]=clf
               report[model_key]=r2_value
           
          with open("artifacts/reports/report_download", 'w') as file:
              json.dump(report_to_send_frontend, file)
          ongoing_add("Training regression models completed")

          with open(self.config.report, 'w') as file:
              json.dump(report, file)
          ongoing_add("Training regression models completed")


          return report
        except Exception as e:
              raise CustomException(e,sys)

         
    def hyper_tune_best_model(self,report,model_type, param_gird ,):
         
       try:  
         ongoing_add("Hyperparameter tuning started")
         logging.info("Hyperparameter tuning for the best model...")
         model =max(report ,key=report.get)
         logging.info(f"Best model: {model} with score: {report[model]}")
         tune_model=model_type[model]
         tuned_model=GridSearchCV(estimator=tune_model , param_grid=param_gird[model] ,verbose=3)
         tuned_model.fit(self.X_train,self.Y_train)
         best_model=tuned_model.best_estimator_
         y_pred=best_model.predict(self.X_test)
         metrics={}
         if (self.type_of_model=="Regressor"):
              metrics['r2_score']=r2_score(self.Y_test,y_pred)
         else:
              
              metrics['clf']=classification_report(self.Y_test,y_pred ,output_dict=True)
         
         joblib.dump(best_model ,os.path.join(self.config.artifacts , "model",self.config.model_path))
        
         prprocess=joblib.load(self.config.preprocess )
         if model!="SLR" and model!="LogisticRegression":
            extract_features_form_data(prprocess ,best_model)
          
          

         logging.info(metrics)  
         with open(self.config.hypertuned_model_report, 'w') as file:
              json.dump(metrics, file)
          
         ongoing_add("Hyperparameter tuning completed")
       except Exception as e:
              raise CustomException(e,sys)

         
    
    def run_Model(self ,type_of_model):
       try:
         self.initialize_the_values(type_of_model )
         report =self.train_model_regressor() if type_of_model=="Regressor" else self.train_model_classifier()
         param_gird=param_grid_all_Regressor if type_of_model=="Regressor" else param_grid_all_classification
         type_of_model=self.config.model_Reg if type_of_model=="Regressor" else self.config.modelClassifier
         final_report =self.hyper_tune_best_model(report,type_of_model,param_gird)
         logging.info(final_report)
         return final_report
       except Exception as e:
              raise CustomException(e,sys)

         
        

              
         


         
         
         






