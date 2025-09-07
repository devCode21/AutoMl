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

#  ongoing_add("Feature engineering started")
#         logging.info("Feature engineering started")
        # checking if any coloums is has more than 30% nULl value 
        
     
         

        # ongoing_add('missing value check completed')
        # self.categorical_cols=
        # categorical_cols_before_ohe=[col for col in self.X_train.columns if self.X_train[col].dtypes=='O']
        # self.numericals_cols=[col for col in self.X_train.columns if self.X_train[col].dtypes !='O']
        # features=self.numericals_cols

        # handling oULier_value with capping for numerical cols 
        # UL=0
        # LL=0
        # ongoing_add('Outlier handling started')
        
          
        # logging.info('Outlier handling completed')
        # ongoing_add('Outlier handling completed')   


    #     ongoing_add('corel started')
    #     # check non linear relationsip also 
    #     # poly= PolynomialFeatures(degree=3)
    #     # num_col=PolynomialFeatures.fit_transform(self.X_train[self.numericals_cols])
    #     # num_col_df=pd.DataFrame(num_col , list(poly.get_feature_names_out))
        
    #     # colliner check
    #     logging.info('corel started')
    #     Xtrain_coliner_check=num_col_df
    #     logging.info(self.numericals_cols)
     

    #     Xtrain_coliner_check['TARGET']=self.y_train
    #     corr=Xtrain_coliner_check.corr()
    #     corr_features={}

        

    #     for col in Xtrain_coliner_check:
    #         if col!='TARGET':
    #             for key,value in corr[col].items():
    #                 if( value >=0.6 and key!='TARGET') and (key not in corr_features):
    #                     corr_features[key]=corr['TARGET'][key]
        
    #     features=sorted(corr_features, key =corr_features.get)
    #     independent_featr=[]
    #     logging.info(f"sorted features {features}")
    #     logging.info(f"inpendepnedt featrues {independent_featr}")
      
    #     for col in self.numerical_cols:
    #          if col not in features and corr['TARGET'][col]>0.1:
    #               logging.info("independent features", col)
    #               independent_featr.append(col)
        
        
    #     ongoing_add(corr_features)
    #     logging.info(corr_features)
    #     ongoing_add('corel completed')  

    #     if len(features)>10:
    #           features_after_colliner_check=list(features[:int(.4*len(features))])+independent_featr
    #     else:   
    #          features_after_colliner_check=list(features[:int(.7*len(features))])+independent_featr  
       
    #     logging.info(f" final features {features_after_colliner_check}")
         
        
    #     # updating nuerical and categorical coloumns 
    #     # numericals_cols_before_vif=features_after_colliner_check
    #     # self.numericals_cols=features_after_colliner_check
    #     # logging.info(self.numericals_cols)

    #     # # replacing the missing value using simpleImupute
    #     # num_pipeline=Pipeline([
    #     #        ("num_impute",SimpleImputer(strategy='mean')),
    #     #        ("scaler", StandardScaler())
    #     #    ])
        
    #     # if(len(features_after_colliner_check)>0):
    #     #        X_train_numeric_cols=num_pipeline.fit_transform(self.X_train[self.numericals_cols])

      
    #     # if len(features_after_colliner_check)>0:
    #     #         X_scaled=pd.DataFrame(X_train_numeric_cols ,columns=self.numericals_cols) 
    #     #         ongoing_add("vif started")
    #     #         flag = True
    #     #         while flag:
    #     #             vif = pd.DataFrame()
    #     #             vif["feature"] = X_scaled.columns
    #     #             vif["VIF"] = [variance_inflation_factor(X_scaled[:10000].values, i) for i in range(X_scaled.shape[1])]
    #     #             print(vif.sort_values(by="VIF", ascending=False))
    #     #             vif_filtered = vif.loc[vif["VIF"] > 10, "feature"]
    #     #             if len(vif_filtered) > 0:
        
    #     #                 features_to_drop = vif.loc[vif["feature"].isin(vif_filtered)].sort_values("VIF", ascending=False)
                        
    #     #                 features_to_drop = features_to_drop["feature"].iloc[:1].tolist()
    #     #                 print(f"Dropping features: {features_to_drop}")
    #     #                 X_scaled = X_scaled.drop(columns=features_to_drop)

    #     #             else:
    #     #                 flag = False
                
    #     #         ongoing_add("vif completed")

    #     #         self.numericals_cols=X_scaled.columns
       
    #     # if len(self.categorical_cols)>0:
              
                
               
    #     #         if(len(self.numericals_cols)>0):
    #     #                 Xtrain_transformed=pd.DataFrame(np.hstack((X_scaled,X_train_categric_cols)) , columns=feature_names)
    #     #         else:
    #     #               Xtrain_transformed=pd.DataFrame(X_train_categric_cols, columns=feature_names)
    #     # else:
    #     #         feature_names=list(self.numericals_cols)
    #     #         Xtrain_transformed=pd.DataFrame(X_scaled , columns=feature_names)

    #     # logging.info(feature_names)  
        
    #     features_mean_value={}
    #     for col in self.X_train.columns:
    #         if self.X_train[col].dtypes=='O':
    #              features_mean_value[col]=self.X_train[col].mode().iloc[0]
    #         else:
    #           features_mean_value[col]=self.X_train[col].mean() 
            

    #     self.preprocess={
    #            "features_before_transfromation":features_mean_value,
    #            "numeric_pipline":num_pipeline,
    #            "categorical_Pipeline":cat_Pipeline,
    #            "thresholds_for_outliers":{"UL":UL, "LL":LL} ,
    #            'numerical_cols':self.numericals_cols,
    #            'categorical_cols':self.categorical_cols,
    #            'categorical_cols_before_ohe':categorical_cols_before_ohe,
    #            'feature_name':list(feature_names),
    #            'numericals_cols_before_vif':numericals_cols_before_vif,
    #            "features":features
    #        }

    #     # ongoing_add("Sampling started")
    #     # Sampling=PipLine2([
    #     #      ('under', RandomUnderSampler(sampling_strategy="not majority")),
    #     #      ('over', SMOTE(sampling_strategy="not minority"))
    #     #     ])
        


    #     # if self.type1<10:
    #     #         X, y = Sampling.fit_resample(Xtrain_transformed,self.y_train)
    #     #         Xtrain_transformed=pd.DataFrame(X ,columns=feature_names)
    #     #         self.y_train=y
    #     #         logging.info(self.y_train)
    #     #         Xtrain_transformed.to_csv("artifacts/transformed_train.csv", index=False)
             
        
    #     # logging.info("vif done")
    #     # joblib.dump(self.preprocess, "artifacts/preprocss.pkl")
    #     # ongoing_add("Sampling completed")
    #     # ongoing_add("X_train transformation completed")
        
    #     return Xtrain_transformed
    #   except Exception as e:
    #       raise CustomException(e,sys)
