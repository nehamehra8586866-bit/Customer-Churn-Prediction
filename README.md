# Customer-Churn-Prediction
Customer Churn Prediction using Machine Learning and Streamlit
-------------------------------------------------------------------
## Project Overview
Customer churn is one of the biggest challenges for telecom companies. This project predicts whether a customer is likely to leave the company (Churn) or stay, using Machine Learning algorithms.
A Streamlit web application is also developed so users can easily enter customer details and get real-time predictions.
--------------------------------------------------------------------
## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Joblib
---------------------------------------------------------------------
##  Dataset
**Dataset:** Telco Customer Churn Dataset
The dataset contains customer information such as:
- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Payment Method
- Monthly Charges
- Total Charges
- Churn (Target Variable)
------------------------------------------------------------------------
##  Project Workflow
1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Model Comparison
9. Model Saving
10. Streamlit Web Application
-------------------------------------------------------------------------
##  Machine Learning Models Used
- Logistic Regression (Baseline)
- Random Forest
- XGBoost
- Support Vector Machine (SVM)
---------------------------------------------------------------------------
## Evaluation Metrics
The models were evaluated using:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
-----------------------------------------------------------------------------
## Best Performing Model
After comparing multiple models, **Support Vector Machine (SVM) with Balanced Class Weight** gave the best overall performance for this dataset by providing a better balance between Precision and Recall.
-----------------------------------------------------------------------------
## Streamlit Application
The application allows users to:
- Enter customer information
- Predict Customer Churn
- View prediction instantly
-----------------------------------------------------------------------------
##  Project Structure
Customer-Churn-Prediction/
│
├── app.py
├── customer_churn.ipynb
├── logistic_model.pkl
├── svm_balanced.pkl
├── scaler.pkl
├── feature_columns.pkl
├── requirements.txt
├── Telco_Customer_Churn.csv
├── Identifying-the-Signs-of-Customer-Churn.png
└── README.md
------------------------------------------------------------------------
##  Installation
Clone the repository
---bash
git clone https://github.com/nehamhera8586866-bit/Customer-Churn-Prediction.git
```
Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

- Hyperparameter Tuning
- Model Deployment
- Explainable AI (SHAP)
- Real-time Prediction API

---

## 👩‍💻 Author

**Neha Mehra**

Aspiring Associate Data Scientist

---

⭐ If you found this project useful, consider giving it a Star!
