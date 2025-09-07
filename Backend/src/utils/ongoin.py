
import os 
def ongoing_add(data ):
    
    with open("artifacts/ongoin.txt" ,'a') as f:
        if type(data)==dict:
            for key,value in data.items():
                f.write(str(key) +str(value) +'\n')
        else:
            f.write(str(data)  + '\n' )
        


# # featuring engineering => remove all nULl values or handle missing values based on mean mdedian mode 
# # train test split 
# # if nULl value is less than 1% X_train remove it or if feture has nULl value more tha 30-40% remove it 
# # replace the value with meadian or mode 
# # then check mULi collinesrt the select 
# # then on the basis of collreation choose only top 20% of components then go on wit X_train transformation for standardisatio and one hot encoduing 
# # the save the self.preprocess file with important features and even piplinse then save the file in format of npy for fast response and csv to send user 
# from src.constant.lib_constant import SimpleImputer ,sys,train_test_split ,Pipeline,PipLine2,dataclass,pd,np,logging,ongoing_add,os,LabelEncoder
# from src.constant.lib_constant import joblib,StandardScaler,SMOTE,RandomUnderSampler,variance_inflation_factor ,CustomException,OneHotEncoder
# from sklearn.preprocessing import PolynomialFeatures
# @dataclass
# class X_trainTransformConfig:
#     artifacts='artifacts'
#     preprocess_X_train='preprocess.pkl',
#     transformed_X_train='X_train.npy'
#     transformed_X_train_csv='transformed.csv'
#     train_X_train='application_train.csv'
  


# class X_trainTransform:
#     def __init__(self):
#         self.config=X_trainTransformConfig()
#         self.X_train=pd.DataFrame()
#         self.X_test=pd.DataFrame()
#         self.y_train=pd.Series()
#         self.y_test=pd.Series()
#         self.categorical_cols=[]
#         self.numerical_cols=[]
#         self.preprocess={}
#         self.type1="" 
#         # encodein y_test abnd y_train
        
        

    
#     def handling_X_train(self,X_train,Target_col ,cols=""):

#      try:
#              # conditiom not hanled what if target was a categorical 
#         ongoing_add("Handling X_train started")
#         logging.info("Handling X_train started")
#         X_train_path=os.path.join(self.config.artifacts , self.config.train_X_train)
#         X_train1=pd.read_csv(X_train)
#         logging.info(cols)
        
#         if(len(cols)>0):
#              logging.info(cols)
#              logging.info(X_train1.columns)

#         self.type1=int(len(X_train1[Target_col].value_counts().values))
#         Y=X_train1[Target_col]
        
#         # emcoding categorical y_values
#         if(X_train1[Target_col].dtype=="O"):
#              y_cat=True,
#              en=LabelEncoder()
#              Y_encode=pd.Series(en.fit_transform(Y))
#              Y=Y_encode
#              logging.info(Y)
#              self.preprocess["le"]=en
        
#         X=X_train1.drop(Target_col ,axis=1)
#         self.X_train ,self.X_test ,self.y_train ,self.y_test=train_test_split(X,Y, test_size=0.2 ,random_state=42)
        
#         logging.info(type(X_train),self.y_train.shape)
#         ongoing_add("Handling X_train completed")
#      except Exception as e:
#          raise CustomException(e,sys)
      


#     def feature_engineering(self):
      
#         ongoing_add("Feature engineering started")
#     # handling missibg values 
#         missing_percent = (self.X_train.isnull().sum() / self.X_train.size) * 100
#         lis = [col for col, pct in missing_percent.items() if pct > 30]
#         if(len(lis)>0):
#             self.X_train.drop(lis , axis=1)

#     # outliers detection 
#         for cols in  self.X_train.columns :
#            if(self.X_train[cols].dtypes !="O"):
#             IQR=self.X_train[cols].quantile(.75)- self.X_train[cols].quantile(.25)
#             UL=1.5*IQR +self.X_train[cols].quantile(.75)
#             LL=self.X_train[cols].quantile(.25)-1.5*IQR

#             self.X_train[cols] =self.X_train[cols].apply(lambda x: UL if x > UL else x)
#             self.X_train[cols]=self.X_train[cols].apply(lambda x:LL if x<LL else x)
#     # numerical data and categoricl differnatly handle
#         categorical_cols_befor_ohe=[col for col in self.X_train.columns if self.X_train[col].dtypes=='O']
#         cat_features_after_ohe=[]
#         cat_Pipeline=Pipeline(steps=[
#                     ('cat_impute', SimpleImputer(strategy='most_frequent')),
#                     ('cat_encode', OneHotEncoder(sparse_output=False))
#              ])
#         if len(categorical_cols_befor_ohe)>0:
             
#              X_train_categric_cols=cat_Pipeline.fit_transform(self.X_train[categorical_cols_befor_ohe])
#              encoder = cat_Pipeline.named_steps['cat_encode']
#              cat_features_after_ohe=list(encoder.get_feature_names_out(categorical_cols_befor_ohe))
            
#     # numerical data =>num_cols_bef_polyFIt 
#         numerical_cols_befor_transform=[col for col in self.X_train.columns if self.X_train[col].dtypes !='O']
#         poly= PolynomialFeatures(degree=3)
#         num_col=poly.fit_transform(self.X_train[numerical_cols_befor_transform])
#         fet=poly.get_feature_names_out(numerical_cols_befor_transform)
#         num_col_df=pd.DataFrame(num_col , columns=fet)

#         # collinearity check 
#         logging.info('corel started')
#         Xtrain_coliner_check=num_col_df.copy()
#         Xtrain_coliner_check['TARGET']=self.y_train
#         corr=Xtrain_coliner_check.corr()
#         corr_features={}
#         for col in Xtrain_coliner_check:
#             if col!='TARGET':
#                 for key,value in corr[col].items():
#                     if( value >=0.6 and key!='TARGET') and (key not in corr_features):
#                         corr_features[key]=corr['TARGET'][key]
        
#         features=sorted(corr_features, key =corr_features.get)
#         independent_featr=[]
#         logging.info(f"sorted features {features}")
#         logging.info(f"inpendepnedt featrues {independent_featr}")
        

#         Xtrain_coliner_check.drop("TARGET",axis=1, inplace=True)
#         for col in Xtrain_coliner_check.columns:
#              if col not in features and corr['TARGET'][col]>0.4:
#                   logging.info("independent features", col)
#                   independent_featr.append(col)
        
#         if len(features)>10:
#               features_after_colliner_check=list(features[:int(.3*len(features))])+independent_featr
#         else:   
#              features_after_colliner_check=list(features[:int(.5*len(features))])+independent_featr  

#         numerical_cols_after_corr=features_after_colliner_check

#         num_pipeline=Pipeline([
#                ("num_impute",SimpleImputer(strategy='mean')),
#                ("scaler", StandardScaler())
#            ])
        
#         final_num_cols=[]
#         if(len(numerical_cols_after_corr)>0):
#               X_train_numeric_cols=num_pipeline.fit_transform(num_col_df[numerical_cols_after_corr])

#               #   vif start here 
#               X_scaled=pd.DataFrame(X_train_numeric_cols , columns=numerical_cols_after_corr)
#               ongoing_add("vif started")
#               flag = True
#               while flag:
#                     vif = pd.DataFrame()
#                     vif["feature"] = X_scaled.columns
#                     vif["VIF"] = [variance_inflation_factor(X_scaled[:10000].values, i) for i in range(X_scaled.shape[1])]
#                     print(vif.sort_values(by="VIF", ascending=False))
#                     vif_filtered = vif.loc[vif["VIF"] > 15, "feature"]
#                     if len(vif_filtered) > 0:
        
#                         features_to_drop = vif.loc[vif["feature"].isin(vif_filtered)].sort_values("VIF", ascending=False)
#                         if(len(features_to_drop)>20):
#                             features_to_drop = features_to_drop["feature"].iloc[:5].tolist()
#                         else:
#                              features_to_drop = features_to_drop["feature"].iloc[:1].tolist()
                             
#                         print(f"Dropping features: {features_to_drop}")
#                         X_scaled = X_scaled.drop(columns=features_to_drop)

#                     else:
#                         flag = False
                
#               ongoing_add("vif completed")
#         final_num_cols=X_scaled.columns
#         final_features=list(final_num_cols)+list(cat_features_after_ohe)
#         if len(categorical_cols_befor_ohe)>0 and len(numerical_cols_befor_transform)>0:
#                 Xtrain_transformed=pd.DataFrame(np.hstack((X_scaled,X_train_categric_cols)) , columns=final_features)
#         else:
#             if(len(numerical_cols_befor_transform)>0):
#                     Xtrain_transformed=pd.DataFrame(X_scaled,columns=final_num_cols)
#             if(len(categorical_cols_befor_ohe)>0):
#                     Xtrain_transformed=pd.DataFrame(X_train_categric_cols,columns=cat_features_after_ohe)
                     
#         # storing mean values of all cols
            
#         features_mean_value={}
#         for col in self.X_train.columns:
#             if self.X_train[col].dtypes=='O':
#                  features_mean_value[col]=self.X_train[col].mode().iloc[0]
#             else:
#               features_mean_value[col]=self.X_train[col].mean() 
        
#         if (len(np.unique(self.y_train))<3):
#                 Sampling=PipLine2([
#                             ('under', RandomUnderSampler(sampling_strategy="not majority")),
#                             ('over', SMOTE(sampling_strategy="not minority"))
#                 ])
#                 X, y = Sampling.fit_resample(Xtrain_transformed,self.y_train)
#                 Xtrain_transformed=pd.DataFrame(X ,columns=final_features)
#                 self.y_train=y
#                 logging.info(self.y_train)
#                 Xtrain_transformed.to_csv("artifacts/transformed_train.csv", index=False)
        
#         self.preprocess={
#                "features_before_transfromation":features_mean_value,
#                "numeric_pipline":num_pipeline,
#                "categorical_Pipeline":cat_Pipeline,
#                "thresholds_for_outliers":{"UL":UL, "LL":LL} ,
#                'numerical_cols_after_vif':final_num_cols,
#                'categorical_cols_afte_ohe':cat_features_after_ohe,
#                'categorical_cols_before_ohe':categorical_cols_befor_ohe,
#                'feature_name':list(final_features),
#                'numericals_cols_before_vif':numerical_cols_after_corr,
#                "features":features,
#                 "numerical_bef_transform":numerical_cols_befor_transform,
#                "ply_fet":fet,
#                "ply":poly
#            }
#         return Xtrain_transformed
            
                  



        



        
        




#     # num cols after corelatio check 
#     # standardisation 
#     # vif 
#     # final_num_cols 

        

    
    
#     def transform_test_data(self):
#       try:
#         ongoing_add("Transforming test data started")
#         if(len(self.preprocess['numericals_cols_before_vif'])>0):
#              X_test_poly=self.preprocess['ply'].transform(self.X_test[self.preprocess['numerical_bef_transform']])
#              X_test=pd.DataFrame(X_test_poly, columns=self.preprocess['ply_fet'])
#              X_test_numeric=X_test[self.preprocess['numericals_cols_before_vif']]
#              X_test_transform_numeric=pd.DataFrame(self.preprocess["numeric_pipline"].transform(X_test_numeric),columns=self.preprocess['numericals_cols_before_vif'])
#              X_test_numpy =X_test_transform_numeric[self.preprocess['numerical_cols_after_vif']].to_numpy()
        
#         if len(list(self.preprocess['categorical_cols_before_ohe']) ) >0:        
#                     X_test_categorical=self.X_test[self.preprocess['categorical_cols_before_ohe']]
#                     X_test_transform_cat=self.preprocess["categorical_Pipeline"].transform(X_test_categorical)
#                     if(self.preprocess['numericals_cols_before_vif']):
#                               X_test_transformed=pd.DataFrame(np.hstack((X_test_numpy,X_test_transform_cat)),columns=self.preprocess["feature_name"])
#                     else:
#                          X_test_transformed=pd.DataFrame(X_test_transform_cat , columns=self.preprocess["feature_name"])
#         else:
#              X_test_transformed=pd.DataFrame(X_test_numpy,columns=self.preprocess["feature_name"])


#         logging.info(f"Transformed test data shape: {X_test_transformed.shape}") 
#         X_test_transformed[self.preprocess['feature_name']].to_csv("transformed_test.csv", index=False)
#         ongoing_add("Transforming test data completed")
#         return X_test_transformed[self.preprocess['feature_name']]
#       except Exception as e:
#           raise CustomException(e ,sys)
           
    

    
#     def run_DataTransformation( self, data , target,cols=""):

#       try:
#         self.handling_X_train(data ,target,cols)
#         Xtrain_transformed=self.feature_engineering()
#         X_test=self.transform_test_data()
#         X_test.to_csv("X.test.csv",index=False)
#         np.save("artifacts/X_train.npy", {"X_train":Xtrain_transformed,"Y_train":self.y_train.values})
#         np.save("artifacts/X_test.npy", {"X_test":X_test,"Y_test":self.y_test.values})
      
#         logging.info(f"Data transformation completed. X_train shape: {self.X_train.shape}, y_train shape: {self.y_train.shape}, X_test shape: {self.X_test.shape}, y_test shape: {self.y_test.shape}")
#         logging.info(f"Transformed data saved to {self.config.transformed_X_train_csv}")
#         # logging.info(type(X_test), type(X_train), type(y_train), type(y_test))
#         # return X_transformed ,y_train ,X_test_tarnsformed ,y_test ,prepreocsee_techniques
#       except Exception as e:
#            raise CustomException(e,sys)    

   
        

            



            

        

        

    
        
    
    





        


     
    