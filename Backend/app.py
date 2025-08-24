from flask import Flask
from flask import send_file ,request
from flask import jsonify
import os
from src.pipelines.train_model_pipline import Train_model_pipline
from src.pipelines.test_model_pipeline import Test_model_pipline
import json
import numpy as np
import joblib
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/Predict_csv_file/<TARGETCOL>/<MODEL_TYPE>', methods=["POST"])
def Predict_csv_file(TARGETCOL,MODEL_TYPE):
    
    data=request.files['file']  # convert bytes to string
    data.save(data.filename)
    print(MODEL_TYPE)
    Train_model_pipline().runTrain_piline(data.filename ,TARGETCOL,"",MODEL_TYPE)
    return "Trained Succesfully",200
    
    


@app.route('/send_form_features', methods=["GET"])
def send_form_features():
    if (not os.path.exists("artifacts/features.npy")):
          return "features not found" ,404
    
    data=np.load("artifacts/features.npy",allow_pickle=True).item()
    return data["form_features"]


@app.route('/predict_form_data', methods=["POST"])
def Predict_form_data():
    if (not os.path.exists("artifacts/features.npy")):
          return "features not found" ,404
    
    data=request.get_json()
    print(type(data))
    pred=Test_model_pipline().run_test_pipeline(data ,'classifier')
    return jsonify({"pred":f"{pred}"})

@app.route('/metrics' ,methods=['GET'])
def get_metrics_of_all_model():
     if (not os.path.exists("artifacts/reports/model_report.json")):
        raise "model report doesnt exist"
    
     with open("artifacts/reports/model_report.json", 'r') as f:
        model_report = json.load(f)
    
     return model_report

@app.route('/ongoing_results', methods=["GET"])

def get_ongoing_res():
    if (not os.path.exists("artifacts/ongoing.json")):
        raise "ongoing results not found"
    
    with open("artifacts/ongoing.json", 'r') as f:
        ongoing_results = json.load(f)
    
    return ongoing_results,200

@app.route('/download_the_tuned_model', methods=["GET"])
def get_tuned_model():
    if(not os.path.exists("artifacts/model/model.pkl")):
        raise "model report doesnt exist"
    
    return send_file("artifacts/model/model.pkl" ,download_name="model.pkl" ,as_attachment=True),200
 


# @app.route('/X_test_transformed', methods=["GET"])
# def get_tuned_model():
#     if(not os.path.exists("artifacts/pred/predicted_data.csv")):
#         raise "model report doesnt exist"
    
#     return send_file("artifacts/pred/predicted_data.csv" ,download_name="pred.csv" ,as_attachment=True),200


@app.route('/download_the_predicts_file', methods=["GET"])
def download_pred_file():
    if (not os.path.exists("artifacts/pred/pred.csv")):
        raise "model report doesnt exist"
    
    path="artifacts/pred/pred.csv"
    return send_file(path),200

    

if __name__=="__main__":
   app.run(debug=True)