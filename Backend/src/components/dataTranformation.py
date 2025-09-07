

# featuring engineering => remove all nULl values or handle missing values based on mean mdedian mode 
# train test split 
# if nULl value is less than 1% X_train remove it or if feture has nULl value more tha 30-40% remove it 
# replace the value with meadian or mode 
# then check mULi collinesrt the select 
# then on the basis of collreation choose only top 20% of components then go on wit X_train transformation for standardisatio and one hot encoduing 
# the save the self.preprocess file with important features and even piplinse then save the file in format of npy for fast response and csv to send user 


from src.constant.lib_constant import SimpleImputer ,sys,train_test_split ,Pipeline,PipLine2,dataclass,pd,np,logging,ongoing_add,os,LabelEncoder
from src.constant.lib_constant import joblib,StandardScaler,SMOTE,RandomUnderSampler,variance_inflation_factor ,CustomException,OneHotEncoder

@dataclass
class X_trainTransformConfig:
    artifacts='artifacts'
    preprocess_X_train='preprocess.pkl',
    transformed_X_train='X_train.npy'
    transformed_X_train_csv='transformed.csv'
    train_X_train='application_train.csv'
  


class X_trainTransform:
    def __init__(self):
        self.config=X_trainTransformConfig()
        self.X_train=pd.DataFrame()
        self.X_test=pd.DataFrame()
        self.y_train=pd.Series()
        self.y_test=pd.Series()
        self.categorical_cols=[]
        self.numerical_cols=[]
        self.preprocess={}
        self.type1="" 
        # encodein y_test abnd y_train
        
        

    
    def handling_X_train(self,X_train,Target_col ,cols=""):

     try:
             # conditiom not hanled what if target was a categorical 
        ongoing_add("Handling X_train started")
        logging.info("Handling X_train started")
        X_train_path=os.path.join(self.config.artifacts , self.config.train_X_train)
        X_train=pd.read_csv(X_train)

        if(cols):
             X_train.drop(cols,inplace=True ,axis=1)

        self.type1=int(len(X_train[Target_col].value_counts().values))
        Y=X_train[Target_col]
        
        # emcoding categorical y_values
        if(X_train[Target_col].dtype=="O"):
             y_cat=True,
             en=LabelEncoder()
             Y_encode=pd.Series(en.fit_transform(Y))
             Y=Y_encode
             logging.info(Y)
             self.preprocess["le"]=en
        
        X=X_train.drop(Target_col ,axis=1)
        self.X_train ,self.X_test ,self.y_train ,self.y_test=train_test_split(X,Y, test_size=0.2 ,random_state=42)
        
        logging.info(type(X_train),self.y_train.shape)
        ongoing_add("Handling X_train completed")
     except Exception as e:
         raise CustomException(e,sys)
      


    def feature_engineering(self):
      try:
        ongoing_add("Feature engineering started")
        logging.info("Feature engineering started")
        # checking if any coloums is has more than 30% nULl value 
        
        missing_percent = (self.X_train.isnull().sum() / self.X_train.size) * 100
        lis = [col for col, pct in missing_percent.items() if pct > 30]
        if(len(lis)>0):
            self.X_train.drop(lis , axis=1)
         

        ongoing_add('missing value check completed')
        self.categorical_cols=[col for col in self.X_train.columns if self.X_train[col].dtypes=='O']
        categorical_cols_before_ohe=[col for col in self.X_train.columns if self.X_train[col].dtypes=='O']
        self.numericals_cols=[col for col in self.X_train.columns if self.X_train[col].dtypes !='O']
        features=self.numericals_cols

        # handling oULier_value with capping for numerical cols 
        UL=0
        LL=0
        ongoing_add('Outlier handling started')
        for cols in  self.numericals_cols:
           IQR=self.X_train[cols].quantile(.75)- self.X_train[cols].quantile(.25)
           UL=1.5*IQR +self.X_train[cols].quantile(.75)
           LL=self.X_train[cols].quantile(.25)-1.5*IQR

           self.X_train[cols] =self.X_train[cols].apply(lambda x: UL if x > UL else x)
           self.X_train[cols]=self.X_train[cols].apply(lambda x:LL if x<LL else x)
          
        logging.info('Outlier handling completed')
        ongoing_add('Outlier handling completed')   


        ongoing_add('corel started')

        # colliner check
        logging.info('corel started')
        Xtrain_coliner_check=self.X_train.copy()
        Xtrain_coliner_check=Xtrain_coliner_check[self.numericals_cols]
        logging.info(self.numericals_cols)
     

        Xtrain_coliner_check['TARGET']=self.y_train
        corr=Xtrain_coliner_check.corr()
        corr_features={}

        

        for col in Xtrain_coliner_check:
            if col!='TARGET':
                for key,value in corr[col].items():
                    if( value >=0.8 and key!='TARGET') and (key not in corr_features):
                        corr_features[key]=corr['TARGET'][key]
        
        features=sorted(corr_features, key =corr_features.get)
        independent_featr=[]
        logging.info(f"sorted features {features}")
        logging.info(f"inpendepnedt featrues {independent_featr}")
      
        for col in self.numerical_cols:
             if col not in features:
                  independent_featr.append(col)
        
        
        ongoing_add(corr_features)
        logging.info(corr_features)
        ongoing_add('corel completed')  

        if len(features)>10:
              features_after_colliner_check=list(features[:int(.5*len(features))])+independent_featr
        else:   
             features_after_colliner_check=features+independent_featr  
       
        logging.info(f" final features {features_after_colliner_check}")
         
        
        # updating nuerical and categorical coloumns 
        numericals_cols_before_vif=features_after_colliner_check
        self.numericals_cols=features_after_colliner_check
        logging.info(self.numericals_cols)

        # replacing the missing value using simpleImupute
        num_pipeline=Pipeline([
               ("num_impute",SimpleImputer(strategy='mean')),
               ("scaler", StandardScaler())
           ])
        
        if(len(features_after_colliner_check)>0):
               X_train_numeric_cols=num_pipeline.fit_transform(self.X_train[self.numericals_cols])

      
        if len(features_after_colliner_check)>0:
                X_scaled=pd.DataFrame(X_train_numeric_cols ,columns=self.numericals_cols) 
                ongoing_add("vif started")
                flag = True
                while flag:
                    vif = pd.DataFrame()
                    vif["feature"] = X_scaled.columns
                    vif["VIF"] = [variance_inflation_factor(X_scaled[:10000].values, i) for i in range(X_scaled.shape[1])]
                    print(vif.sort_values(by="VIF", ascending=False))
                    vif_filtered = vif.loc[vif["VIF"] > 30, "feature"]
                    if len(vif_filtered) > 0:
        
                        features_to_drop = vif.loc[vif["feature"].isin(vif_filtered)].sort_values("VIF", ascending=False)
                        
                        features_to_drop = features_to_drop["feature"].iloc[:2].tolist()
                        print(f"Dropping features: {features_to_drop}")
                        X_scaled = X_scaled.drop(columns=features_to_drop)

                    else:
                        flag = False
                
                ongoing_add("vif completed")

                self.numericals_cols=X_scaled.columns
        cat_Pipeline=Pipeline(steps=[
                    ('cat_impute', SimpleImputer(strategy='most_frequent')),
                    ('cat_encode', OneHotEncoder(sparse_output=False))
                ])
        if len(self.categorical_cols)>0:
              
                
                X_train_categric_cols=cat_Pipeline.fit_transform(self.X_train[self.categorical_cols])

                encoder = cat_Pipeline.named_steps['cat_encode']
                feature_names = list(self.numericals_cols)+list(encoder.get_feature_names_out(self.categorical_cols))
                self.categorical_cols=list(encoder.get_feature_names_out(self.categorical_cols))
                if(len(self.numericals_cols)>0):
                        Xtrain_transformed=pd.DataFrame(np.hstack((X_scaled,X_train_categric_cols)) , columns=feature_names)
                else:
                      Xtrain_transformed=pd.DataFrame(X_train_categric_cols, columns=feature_names)
        else:
                feature_names=list(self.numericals_cols)
                Xtrain_transformed=pd.DataFrame(X_scaled , columns=feature_names)

        logging.info(feature_names)  
        
        features_mean_value={}
        for col in self.X_train.columns:
            if self.X_train[col].dtypes=='O':
                 features_mean_value[col]=self.X_train[col].mode().iloc[0]
            else:
              features_mean_value[col]=self.X_train[col].mean() 
            

        preprocess1={
               "features_before_transfromation":features_mean_value,
               "numeric_pipline":num_pipeline,
               "categorical_Pipeline":cat_Pipeline,
               "thresholds_for_outliers":{"UL":UL, "LL":LL} ,
               'numerical_cols':self.numericals_cols,
               'categorical_cols':self.categorical_cols,
               'categorical_cols_before_ohe':categorical_cols_before_ohe,
               'feature_name':list(feature_names),
               'numericals_cols_before_vif':numericals_cols_before_vif,
               "features":features
           }
        self.preprocess=self.preprocess|preprocess1

        ongoing_add("Sampling started")
        Sampling=PipLine2([
             ('under', RandomUnderSampler(sampling_strategy="not majority")),
             ('over', SMOTE(sampling_strategy="not minority"))
            ])
        


        if self.type1<10:
                X, y = Sampling.fit_resample(Xtrain_transformed,self.y_train)
                Xtrain_transformed=pd.DataFrame(X ,columns=feature_names)
                self.y_train=y
                logging.info(self.y_train)
                Xtrain_transformed.to_csv("artifacts/transformed_train.csv", index=False)
             
        
        logging.info("vif done")
        joblib.dump(self.preprocess, "artifacts/preprocss.pkl")
        ongoing_add("Sampling completed")
        ongoing_add("X_train transformation completed")
        
        return Xtrain_transformed
      except Exception as e:
          raise CustomException(e,sys)

    
    
    def transform_test_data(self):
      try:
        ongoing_add("Transforming test data started")
        if(len(self.numericals_cols)>0):
             X_test_numeric=self.X_test[self.preprocess['numericals_cols_before_vif']]
             X_test_transform_numeric=pd.DataFrame(self.preprocess["numeric_pipline"].transform(X_test_numeric),columns=self.preprocess['numericals_cols_before_vif'])
             X_test_numpy =X_test_transform_numeric[self.numericals_cols].to_numpy()
        
        if len(list(self.categorical_cols) ) >0:        
                    X_test_categorical=self.X_test[self.preprocess['categorical_cols_before_ohe']]
                    X_test_transform_cat=self.preprocess["categorical_Pipeline"].transform(X_test_categorical)
                    if(len(self.numericals_cols)>0):
                              X_test_transformed=pd.DataFrame(np.hstack((X_test_numpy,X_test_transform_cat)),columns=self.preprocess["feature_name"])
                    else:
                         X_test_transformed=pd.DataFrame(X_test_transform_cat , columns=self.preprocess["feature_name"])
        else:
             X_test_transformed=pd.DataFrame(X_test_numpy,columns=self.preprocess["feature_name"])


        logging.info(f"Transformed test data shape: {X_test_transformed.shape}") 
        X_test_transformed[self.preprocess['feature_name']].to_csv("transformed_test.csv", index=False)
        ongoing_add("Transforming test data completed")
        return X_test_transformed[self.preprocess['feature_name']]
      except Exception as e:
          raise CustomException(e ,sys)
           
    

    
    def run_DataTransformation( self, data , target,cols=""):

      try:
        self.handling_X_train(data ,target,cols)
        Xtrain_transformed=self.feature_engineering()
        X_test=self.transform_test_data()
        X_test.to_csv("X.test.csv",index=False)
        np.save("artifacts/X_train.npy", {"X_train":Xtrain_transformed,"Y_train":self.y_train.values})
        np.save("artifacts/X_test.npy", {"X_test":X_test,"Y_test":self.y_test.values})
      
        logging.info(f"Data transformation completed. X_train shape: {self.X_train.shape}, y_train shape: {self.y_train.shape}, X_test shape: {self.X_test.shape}, y_test shape: {self.y_test.shape}")
        logging.info(f"Transformed data saved to {self.config.transformed_X_train_csv}")
        # logging.info(type(X_test), type(X_train), type(y_train), type(y_test))
        # return X_transformed ,y_train ,X_test_tarnsformed ,y_test ,prepreocsee_techniques
      except Exception as e:
           raise CustomException(e,sys)    

   
        

            



            

        

        

    
        
    
    





        


     
    