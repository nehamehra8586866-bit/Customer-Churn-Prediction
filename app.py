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