from src.constant.lib_constant import dataclass ,logging ,ongoing_add,os ,np,pd ,CustomException ,sys
@dataclass

class DataIngesConfig:
    artifacts='artifacts'
  

@dataclass
class DataIngestion():
    config=DataIngesConfig()
   
    
    def store_data(self , data, data_file_name="Train_data" ):
        # data would come in csv right 
        # read how many categorical and numerical columns are there ans store in csv an npy 
     try:
            logging.info("DATA INGESTION STARTED")
            ongoing_add("Data Ingestion Started")
            df=pd.read_csv(data)
            shape =df.shape
            categorical_cols=[col for col in df.columns if df[col].dtypes=='O']
            numericals_cols=[col for col in df.columns if df[col].dtypes !='O']
            logging.info(f"Shape of the data is {shape}")
            logging.info(f"Categorical columns are {categorical_cols}") 
            logging
            df.to_csv(os.path.join(self.config.artifacts,f'{data_file_name}.csv' ))
            np.save(os.path.join(self.config.artifacts,f'{data_file_name}.npy'),df)

            logging.info("DATA INGESTION COMPLETED")
            ongoing_add("Data Ingestion Completed")
            
            ongoing_add(f"Data Ingestion Completed with shape {shape} and categorical columns {categorical_cols} and numerical columns {numericals_cols}")

            return shape , categorical_cols, numericals_cols , df
     except Exception as e:
         raise CustomException(e,sys)
    
# working fine 