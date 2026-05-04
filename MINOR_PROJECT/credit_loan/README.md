# 💰 Loan Approval Prediction System

An end-to-end Machine Learning project that predicts whether a loan should be approved based on applicant financial and demographic details.

---

## 🚀 Project Overview

Banks face two major challenges:
- ❌ Rejecting good customers → loss of business  
- ❌ Approving risky customers → financial loss  

This project builds a predictive system to **balance risk and approval decisions** using Machine Learning.

---

## 🎯 Objective

To develop a model that:
- Minimizes **false approvals (risky customers)**
- Minimizes **false rejections (good customers)**
- Provides **interpretable predictions**

---

## 🧠 Models Used

- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Naive Bayes  
- Support Vector Machine (SVM)  
- 🌟 **Random Forest (Best Model)**  

---

## 🏆 Best Model: Random Forest

Random Forest was selected based on:

- ✔ Highest F1 Score  
- ✔ Balanced Precision & Recall  
- ✔ Lowest False Negatives  
- ✔ Strong business alignment  

---

## 📊 Evaluation Metrics

- Accuracy  
- Precision (Primary focus)  
- Recall  
- F1 Score  
- Confusion Matrix  

---

## 📂 Features Used

### 🔢 Numerical Features
- Applicant Income  
- Coapplicant Income  
- Age  
- Dependents  
- Credit Score  
- Existing Loans  
- Debt-to-Income Ratio (DTI)  
- Savings  
- Collateral Value  
- Loan Amount  
- Loan Term  

### 🏷️ Categorical Features
- Employment Status  
- Marital Status  
- Education Level  
- Gender  
- Employer Category  
- Property Area  
- Loan Purpose  

---

## ⚙️ Data Processing

- Label Encoding (for binary categories)  
- One-Hot Encoding (for categorical features)  
- Feature alignment using `reindex()`  

---

## 🖥️ Streamlit Application

A fully interactive web app was built using Streamlit:

### ✨ Features
- User-friendly input form  
- Tooltip help (`?`) for each feature  
- Real-time prediction  
- Confidence score display  
- Risk classification:
  - 🟢 Low Risk  
  - 🟡 Moderate Risk  
  - 🔴 High Risk  
- Feature importance visualization  

---

## 📊 Feature Importance

The model highlights key decision factors such as:
- Credit Score  
- Debt-to-Income Ratio  
- Applicant Income  
- Loan Amount  

---
 How to Run

### 1️⃣ Clone the repository

### 2️⃣ pip install -r requirements.txt

### 3️⃣ streamlit run app.py

---
### 🔗 Live App

👉 https://creditloan-application01.streamlit.app/