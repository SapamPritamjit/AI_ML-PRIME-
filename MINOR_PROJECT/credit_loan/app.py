import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np
import os

# -----------------------------
# Load Model
# -----------------------------
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "rf_model.pkl")

model = joblib.load(model_path)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Loan Approval System",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Loan Approval Prediction System")
st.markdown("### AI-powered decision system for loan approval")

# -----------------------------
# Input Section
# -----------------------------
st.subheader("📋 Applicant Information")

col1, col2 = st.columns(2)

with col1:
    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0,
        help="Monthly income of the applicant (higher income increases approval chances)"
    )

    coapplicant_income = st.number_input(
        "Coapplicant Income",
        min_value=0,
        help="Monthly income of co-applicant, if any"
    )

    age = st.number_input(
        "Age",
        min_value=18,
        help="Applicant's age (must be at least 18)"
    )

    dependents = st.number_input(
        "Dependents",
        min_value=0,
        help="Number of people financially dependent on the applicant"
    )

    credit_score = st.number_input(
        "Credit Score",
        min_value=0,
        help="Indicates repayment history (300–900). Higher = better approval chances"
    )

with col2:
    existing_loans = st.number_input(
        "Existing Loans",
        min_value=0,
        help="Number of currently active loans"
    )

    dti_ratio = st.number_input(
        "DTI Ratio",
        min_value=0.0,
        help="Debt-to-Income ratio = total debt / income. Lower is better (e.g., <0.4 ideal)"
    )

    savings = st.number_input(
        "Savings",
        min_value=0,
        help="Total savings available (higher savings improves approval chances)"
    )

    collateral_value = st.number_input(
        "Collateral Value",
        min_value=0,
        help="Value of asset pledged against loan (e.g., house, property)"
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        help="Total loan amount requested"
    )

    loan_term = st.number_input(
        "Loan Term (months)",
        min_value=1,
        help="Duration of loan repayment in months"
    )

# -----------------------------
# Categorical Inputs
# -----------------------------
st.subheader("📊 Additional Details")

col3, col4 = st.columns(2)

with col3:
    employment = st.selectbox(
        "Employment Status",
        ["Salaried", "Self-Employed", "Business"],
        help="Type of employment of the applicant"
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married"],
        help="Marital status of the applicant"
    )

    education = st.selectbox(
        "Education Level",
        ['Not Graduate', 'Graduate'],
        help="Indicates whether the applicant has completed a graduate degree"
    )

with col4:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
        help="Applicant's gender"
    )

    employer_category = st.selectbox(
        "Employer Category",
        ["Govt", "Private", "Self"],
        help="Type of employer organization"
    )

    property_area = st.selectbox(
        "Property Area",
        ["Urban", "Semi-Urban", "Rural"],
        help="Location type of property"
    )

    loan_purpose = st.selectbox(
        "Loan Purpose",
        ["Personal", "Car", "Business", "Home", "Education"],
        help="Reason for taking the loan"
    )
    

# -----------------------------
# Predict Button
# -----------------------------
if st.button("🔍 Predict Loan Status"):

    # -----------------------------
    # Create DataFrame
    # -----------------------------
    input_data = pd.DataFrame({
        "Applicant_Income": [applicant_income],
        "Coapplicant_Income": [coapplicant_income],
        "Age": [age],
        "Dependents": [dependents],
        "Credit_Score": [credit_score],
        "Existing_Loans": [existing_loans],
        "DTI_Ratio": [dti_ratio],
        "Savings": [savings],
        "Collateral_Value": [collateral_value],
        "Loan_Amount": [loan_amount],
        "Loan_Term": [loan_term],
        "Employment_Status": [employment],
        "Marital_Status": [marital_status],
        "Education_Level": [education],
        "Gender": [gender],
        "Employer_Category": [employer_category],
        "Property_Area": [property_area],
        "Loan_Purpose": [loan_purpose]
    })

    # -----------------------------
    # Encoding
    # -----------------------------
    input_encoded = pd.get_dummies(input_data)
    input_encoded = input_encoded.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    # -----------------------------
    # Prediction (with spinner)
    # -----------------------------
    with st.spinner("Analyzing application..."):
        prediction = model.predict(input_encoded)[0]
        probability = model.predict_proba(input_encoded)[0][1]

    # -----------------------------
    # Warning
    # -----------------------------
    if credit_score == 0:
        st.warning("⚠️ Credit score is important for accurate prediction")

    # -----------------------------
    # Output
    # -----------------------------
    st.subheader("📈 Prediction Result")

    if prediction == 1:
        st.success(f"✅ Loan Approved (Confidence: {probability:.2%})")
    else:
        st.error(f"❌ Loan Rejected (Confidence: {1 - probability:.2%})")

    # -----------------------------
    # Feature Importance
    # -----------------------------
    st.subheader("📊 Feature Importance")

    try:
        # import matplotlib.pyplot as plt
        # import numpy as np

        # Get model
        try:
            rf_model = model.named_steps["rf"]
        except:
            rf_model = model

        importances = rf_model.feature_importances_
        feature_names = model.feature_names_in_

        # Sort top 10
        indices = np.argsort(importances)[-10:][::-1]

        top_features = [feature_names[i] for i in indices]
        top_importances = importances[indices]

        # Color gradient (important!)
        colors = plt.cm.Greens(np.linspace(0.4, 1, len(indices)))

        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor('#f8f9fa')  # light background

        bars = ax.barh(range(len(indices)), top_importances, color=colors)

        # Labels
        ax.set_yticks(range(len(indices)))
        ax.set_yticklabels(top_features, fontsize=11)
        ax.invert_yaxis()

        ax.set_xlabel("Importance Score", fontsize=12)
        ax.set_title("Top Features Driving Loan Approval", fontsize=14, fontweight="bold")

        # Value labels
        for i, v in enumerate(top_importances):
            ax.text(v + 0.003, i, f"{v:.3f}", va='center', fontsize=10)

        # Clean UI
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.grid(axis='x', linestyle='--', alpha=0.3)

        plt.tight_layout()

        st.pyplot(fig)

    except:
        st.warning("Feature importance not available")

    # -----------------------------
    # Risk Analysis (ALWAYS SHOW)
    # -----------------------------
    st.subheader("📊 Risk Assessment")

    if probability > 0.75:
        st.success("🟢 Low Risk Applicant")
    elif probability > 0.5:
        st.warning("🟡 Moderate Risk Applicant")
    else:
        st.error("🔴 High Risk Applicant")