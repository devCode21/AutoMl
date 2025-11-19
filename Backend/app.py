from flask import Flask
from flask import send_file ,request
from flask import jsonify
import os
from src.pipelines.train_model_pipline import Train_model_pipline
from src.pipelines.test_model_pipeline import Test_model_pipline
import json
import numpy as np
import joblib
import pandas as pd 
from flask_cors import CORS
from flask import session
from src.logger import logging
app=Flask(__name__)
app.secret_key = 'supersecret123'  # Add a secret key for session management
CORS(app , supports_credentials=True , origins=["*"] ) #))


# training -api


@app.route('/Predict_csv_file', methods=['POST'])
def Predict_csv_file():
    TARGET_COL1 = session.get('target_col')
    MODEL_TYPE1 = session.get('model_type')
    File_Name = session.get('file_name')
    Col = request.get_json().get('columns')
   
    print("Session after /Data:", dict(session))
    logging.info(f"target column is {TARGET_COL1}, model type is {MODEL_TYPE1}, file name is {File_Name}")
    
    Train_model_pipline().runTrain_piline(File_Name, TARGET_COL1, Col, MODEL_TYPE1)
    return "Trained Successfully", 200


@app.route('/Data/<TARGETCOL>/<MODEL_TYPE>', methods=["POST"])
def get_cols(TARGETCOL, MODEL_TYPE):
    data = request.files['file']
    data.save(data.filename)

    session['target_col'] = TARGETCOL
    session['model_type'] = MODEL_TYPE
    session['file_name'] = data.filename
    print("Session after /Data:", dict(session))
    df = pd.read_csv(data.filename)
    if TARGETCOL not in df.columns:
        return "target column not found", 404

    df = df.drop(TARGETCOL, axis=1)   # drop properly
    return jsonify(list(df.columns)), 200



# important features 
@app.route('/send_form_features', methods=["GET"])
def send_form_features():
    if (not os.path.exists("artifacts/features.npy")):
          return "features not found" ,404
    
    data=np.load("artifacts/features.npy",allow_pickle=True).item()
    return data["form_features"]


# testing the model for form data 
@app.route('/predict_form_data', methods=["POST"])
def Predict_form_data():
    if (not os.path.exists("artifacts/features.npy")):
          return "features not found" ,404
    
    data=request.get_json()
    print(type(data))
    pred=Test_model_pipline().run_test_pipeline(data ,'')
    return jsonify({"pred":f"{pred}"})


# api for metrics for ui 
@app.route('/metrics' ,methods=['GET'])
def get_metrics_of_all_model():
     if (not os.path.exists("artifacts/reports/model_report.json")):
        raise "model report doesnt exist"
    
     with open("artifacts/reports/model_report.json", 'r') as f:
        model_report = json.load(f)
    
     return model_report


# api for download metrics
@app.route('/download_metrics' ,methods=['GET'])
def download_metrics():
    if (not os.path.exists("artifacts/reports/report_download.json")):
         return "model doesnt exist ",404
    with open('artifacts/reports/report_download.json','r') as f:
        model_report=json.load(f)
    
    return send_file("artifacts/reports/report_download.json",as_attachment=True , download_name='report.json'),200

# api for intermediate results 
@app.route('/ongoing_results', methods=["GET"])
def get_ongoing_res():
    if (not os.path.exists("artifacts/ongoing.json")):
        raise "ongoing results not found"
    
    with open("artifacts/ongoing.json", 'r') as f:
        ongoing_results = json.load(f)
    
    return ongoing_results,200

# donwloading best tune model 
@app.route('/download_the_tuned_model', methods=["GET"])
def get_tuned_model():
    if(not os.path.exists("artifacts/model/model.pkl")):
        raise "model report doesnt exist"
    
    return send_file("artifacts/model/model.pkl" ,download_name="model.pkl" ,as_attachment=True),200
 

# to download the transformed data 
@app.route('/X_test_transformed', methods=["GET"])
def get_transformed_trained_dataset():
    if(not os.path.exists("artifacts/transformed_train.csv")):
        raise "model report doesnt exist"
    
    return send_file("artifacts/transformed_train.csv" ,download_name="pred.csv" ,as_attachment=True),200



# to testing of test csv data 
@app.route('/download_the_predicts_file', methods=["POST"])
def download_pred_file():
    data=request.files['file']
    data.save(data.filename)
    Test_model_pipline().run_test_pipeline(data.filename ,'Regressor')
    if (not os.path.exists("artifacts/pred/predicted_data.csv")):
        return "file was not found" ,404
    
    path="artifacts/pred/predicted_data.csv"
    return 'Success', 200


@app.route('/download_pred_file', methods=["GET"])
def download_files():
    if (not os.path.exists("artifacts/pred/predicted_data.csv")):
        return "file was not found" ,404
    
    path="artifacts/pred/predicted_data.csv"
    return send_file(path, as_attachment=True ,download_name='pred.csv'),200  





if __name__=="__main__":
   app.run(host="0.0.0.0" ,debug=True)