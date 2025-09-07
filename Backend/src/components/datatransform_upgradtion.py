# # firts handle outliers and missing and enocode it 
# # then => build a xgbbosst and lr check for whicb if perofrms betetr choose the top performin dataset from them 
# # then start perprocessing etc ... one by one 
# from dataclasses import dataclass
# from sklearn.model_selection import cross_val_score, KFold
# from sklearn.linear_model import LogisticRegression ,LinearRegression
# from sklearn.ensemble import RandomForestClassifier ,RandomForestRegressor 

# import pandas as pd 
# from sklearn.preprocessing import LabelEncoder
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.pipeline import Pipeline
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import StandardScaler 
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.metrics import accuracy_score ,r2_score
# class get_best_features:
#     def __init__(self):
#          self.X_train =pd.DataFrame()
#          self.y_train=[]
#          self.X_test=pd.DataFrame()
#          self.y_test=[]
        

#     def handle_data(self):
#          data =pd.read_csv('artifacts/Train_data.csv')
#          X=data.drop('Price', axis=1)
#          y=data['Price']
#          le = LabelEncoder()
#          y = le.fit_transform(y)
         
#          self.X_train , self.X_test , self.y_train ,self.y_test=train_test_split(X, y ,test_size=0.3 ,random_state=42)
#          print(self.X_train.shape ,self.y_train.shape)
#          return le 

#     def preprocess_data (self):
       
#         # outlier detection 

#           for cols in  self.X_train.columns :
#             if(self.X_train[cols].dtypes !="O" and len(self.X_train[cols].value_counts())>2):
#              IQR=self.X_train[cols].quantile(.75)- self.X_train[cols].quantile(.25)
#              UL=1.5*IQR +self.X_train[cols].quantile(.75)
#              LL=self.X_train[cols].quantile(.25)-1.5*IQR
#              self.X_train[cols] =self.X_train[cols].apply(lambda x: UL if x > UL else x)
#              self.X_train[cols]=self.X_train[cols].apply(lambda x:LL if x<LL else x)
        
         
#           num_pipeline=Pipeline([('impute' , SimpleImputer(strategy='median')) ,('transform', StandardScaler())])
#           cat_pipeline=Pipeline([('encode', OneHotEncoder(sparse_output=False))])
#           categorical_cols=[cols for cols in self.X_train.columns if self.X_train[cols].dtype=='O']
#           numerical_cols=[cols for cols in self.X_train.columns if self.X_train[cols].dtype!='O']

#           preprocessor = ColumnTransformer([
#                          ('num', num_pipeline, numerical_cols),
#                          ('cat', cat_pipeline, categorical_cols)
#           ])
#           X_train_tarnsformed=preprocessor.fit_transform(self.X_train)
#           X_test_tarnsformed=preprocessor.transform(self.X_test)
         
#           cat_encoded_cols=[]
#           if((len(categorical_cols))>0):
#            ohe = preprocessor.named_transformers_['cat']['encode']  
#            cat_encoded_cols = ohe.get_feature_names_out(categorical_cols)
#           cols=list(numerical_cols)+list(cat_encoded_cols)
#           return X_train_tarnsformed ,X_test_tarnsformed ,cols
    

#     def predict_LR(self , X, X_test , cols):
#         k=KFold(n_splits=20 , shuffle=True , random_state=42)
#         cross_val_score(LinearRegression(), X ,self.y_train ,verbose=3 , cv=k , scoring='r2')
#         model=LinearRegression()
#         model.fit(X , self.y_train)
#         y_pred=model.predict(X_test)
#         acc=r2_score(self.y_test , y_pred)
#         print(acc)

#         a=model.coef_.ravel()
#         dict1={}
#         for i in range(0, len(cols)):
#             dict1[cols[i]]=a[i]
        
#         keys =sorted(dict1 , key=dict1.get , reverse=True)
#         return keys , acc
    
#     def predict_RF(self , X, X_test , cols):
#         k=KFold(n_splits=20 , shuffle=True , random_state=42)
#         cross_val_score(RandomForestRegressor(), X ,self.y_train ,verbose=3 , cv=k , scoring='r2')
#         model=RandomForestClassifier(n_jobs=-1)
#         model.fit(X , self.y_train)
#         y_pred=model.predict(X_test)
#         acc=r2_score(self.y_test , y_pred)
#         print(acc)
#         a=model.feature_importances_
#         dict1={}
#         for i in range(0, len(cols)):
#             dict1[cols[i]]=a[i]
        
#         keys =sorted(dict1 , key=dict1.get , reverse=True)
#         return keys , acc
#     def most_import_features(self,key1 ,key2):
#         imp_features = key1[:int(0.4*len(key1))] + [f for f in key2[:int(0.4*len(key1))] if f not in key1[:int(0.4*len(key1))]]
#         return imp_features

#     def run(self):
#         le=self.handle_data()
#         X ,X_test ,cols=self.preprocess_data()
#         a , b=self.predict_LR(X ,X_test,cols)
#         c ,d=self.predict_RF(X ,X_test , cols)
#         imp_features=self.most_import_features(a,c)
#         return imp_features ,self.X_train ,self.X_test,self.y_test, self.y_train ,le
    
