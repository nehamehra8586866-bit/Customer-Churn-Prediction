from pyexpat import model

import streamlit as st
import pandas as pd
import numpy as np
import joblib


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

logistic_model = joblib.load("logistic_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")


st.image("Identifying-the-Signs-of-Customer-Churn.png")


st.title("📊 Customer Churn Prediction System")

st.info(
    "Enter the customer's information below and click **Predict** to check the likelihood of customer churn."
)

st.markdown("""
Predict whether a telecom customer is likely to **Churn** or **Stay** using a trained Machine Learning model.
""")

st.divider()


st.header("Customer Information")


col1, col2 = st.columns(2)
with col1:

    gender = st.selectbox("Gender", ["Male", "Female"])

    senior = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    phone = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    multiple = st.selectbox(
        "Multiple Lines",
        ["No", "Yes"]
    )

    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

with col2:

    security = st.selectbox(
        "Online Security",
        ["No", "Yes"]
    )

    backup = st.selectbox(
        "Online Backup",
        ["No", "Yes"]
    )

    device = st.selectbox(
        "Device Protection",
        ["No", "Yes"]
    )

    support = st.selectbox(
        "Tech Support",
        ["No", "Yes"]
    )

    tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes"]
    )

    movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes"]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    max_value=100,
    value=12
)

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=840.0
)

predict = st.button(
    "🔍 Predict Customer Churn",
    use_container_width=True
)

if predict:

    input_data = pd.DataFrame(0, index=[0], columns=feature_columns)

    input_data["gender"] = gender
    input_data["SeniorCitizen"] = senior
    input_data["Partner"] = partner
    input_data["Dependents"] = dependents
    input_data["tenure"] = tenure
    input_data["PhoneService"] = phone
    input_data["MultipleLines"] = multiple
    input_data["OnlineSecurity"] = security
    input_data["OnlineBackup"] = backup
    input_data["DeviceProtection"] = device
    input_data["TechSupport"] = support
    input_data["StreamingTV"] = tv
    input_data["StreamingMovies"] = movies
    input_data["PaperlessBilling"] = paperless
    input_data["MonthlyCharges"] = monthly
    input_data["TotalCharges"] = total

    if internet == "Fiber optic":
        input_data["InternetService_Fiber optic"] = 1
    elif internet == "No":
        input_data["InternetService_No"] = 1

    if contract == "One year":
        input_data["Contract_One year"] = 1
    elif contract == "Two year":
        input_data["Contract_Two year"] = 1

    if payment == "Credit card (automatic)":
        input_data["PaymentMethod_Credit card (automatic)"] = 1
    elif payment == "Electronic check":
        input_data["PaymentMethod_Electronic check"] = 1
    elif payment == "Mailed check":
        input_data["PaymentMethod_Mailed check"] = 1

    input_data["gender"] = input_data["gender"].map({"Male": 1, "Female": 0})

    input_data["SeniorCitizen"] = input_data["SeniorCitizen"].map({"Yes": 1, "No": 0})

    yes_no_cols = [
        "Partner",
        "Dependents",
        "PhoneService",
        "MultipleLines",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "PaperlessBilling"
    ]

    for col in yes_no_cols:
        input_data[col] = input_data[col].map({"Yes": 1, "No": 0})

    input_scaled = scaler.transform(input_data)

    prediction = logistic_model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer is likely to Stay")
