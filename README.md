

# AutoML – Automating Your Machine Learning Journey

AutoML is an AI-powered web application that **automates the end-to-end Machine Learning pipeline** from any CSV dataset.

Currently, it supports **Supervised ML problems** such as **Classification** and **Regression**.
In upcoming versions, support for **Unsupervised Learning** and **Neural Networks** will also be added.

---

## 🚀 Features

* 📂 **Data Ingestion** – Upload CSV/Excel files, select target columns, and remove unnecessary columns.
* 🧹 **Data Preprocessing** –

  * Handle **missing values** and **outliers**
  * Detect and remove **multicollinearity** (feature correlation & VIF check)
  * Feature selection (retain top 60–70% features)
  * Encode categorical variables
  * Standardization / Normalization
  * Handle **imbalanced data** (sampling techniques)
  * Prevent **data leakage** using pipelines
  * Store preprocessing steps in `.pkl` for reusability
* 🤖 **Model Building** –

  * Train multiple models (based on problem type: classification/regression)
  * Select the **best model** based on evaluation metrics (Accuracy, R² score, etc.)
  * Apply **hyperparameter tuning**
  * Save the best trained model as `.pkl`
* 📊 **Model Reports & Predictions** –

  * Compare performance of different models
  * Download model reports, transformed datasets, and prediction results as CSV
* ⚡ **Real-time Predictions** – Upload new data and get instant predictions.

---

## 🛠️ Tech Stack

### Backend

* **Flask** (REST APIs)

  * Endpoints:

    * `model_prediction`
    * `csv_file_download`
    * `report_download`
    * `transformed_data_download`

### Frontend

* **React (Vite.js)**

  * **Home Page** – Overview of project and features
  * **Training Page** – Upload CSV, select target columns, configure training
  * **Reports Page** – Compare models, view/download reports and predictions
  * **CSV Upload** – Upload test dataset and download predicted results
  * **Real-time Predictions** – Enter feature values manually and get instant predictions

---

## 📂 Project Workflow

1. **Upload Dataset** → Select target column(s)
2. **Preprocessing** → Cleaning, feature engineering, transformations
3. **Model Training** → Multiple models trained & best one selected
4. **Evaluation** → Model comparison using metrics
5. **Save & Deploy** → Best model saved as `.pkl` and used for predictions
6. **Prediction** → Upload test CSV or input values manually to get results

---



## 📸 Screenshots 

<img width="1862" height="928" alt="Screenshot 2025-09-21 234221" src="https://github.com/user-attachments/assets/9faa56d8-f334-41a0-853d-9f64aa97f837" />
<img width="1419" height="791" alt="Screenshot 2025-09-21 234347" src="https://github.com/user-attachments/assets/77c10abe-a132-41d4-8d32-35445ca51cb5" />
<img width="1075" height="867" alt="Screenshot 2025-09-21 234544" src="https://github.com/user-attachments/assets/077ed3bd-1dab-4467-be9d-a917cb4e5c73" />
<img width="1175" height="812" alt="Screenshot 2025-09-21 234209" src="https://github.com/user-attachments/assets/2f2f9c19-81cb-4794-a9c6-7ce9776e7e3e" />
<img width="774" height="788" alt="Screenshot 2025-09-21 234611" src="https://github.com/user-attachments/assets/39411141-233b-4ae8-9dbf-c8a807e6664c" />
<img width="1885" height="839" alt="Screenshot 2025-09-21 234556" src="https://github.com/user-attachments/assets/0aae3dc0-9531-4ee2-b58d-6e22c43df7fd" />
<img width="1075" height="867" alt="Screenshot 2025-09-21 234544" src="https://github.com/user-attachments/assets/077ed3bd-1dab-4467-be9d-a917cb4e5c73" />










---

## 📌 Future Work

* Add **Unsupervised Learning** (Clustering, Dimensionality Reduction)
* Integrate **Deep Learning models** (Neural Networks)
* Improve **Auto metric selection** for problem-specific evaluation
* Enhance **Explainability (XAI)** with SHAP/Feature importance visualizations

--
