# 🛒 ShopSmart Analytics

A Machine Learning powered Streamlit web application that predicts whether a visitor is likely to make a purchase on an e-commerce website based on browsing behavior.

---

# 📌 Project Overview

ShopSmart Analytics helps e-commerce businesses understand customer behavior and predict purchase intention using machine learning.

The application analyzes:

- User browsing activity
- Product page interactions
- Time spent on website
- Bounce rates
- Exit rates
- Visitor type
- Traffic source
- Seasonal shopping behavior

---

# 🚀 Features

✅ Beautiful modern Streamlit UI  
✅ Real-time purchase prediction  
✅ Interactive input form  
✅ Feature descriptions using tooltips (?)  
✅ About page included  
✅ Machine Learning model integration  
✅ Responsive layout  
✅ Dark modern theme  

---

# 🤖 Machine Learning Model

The project uses:

- Random Forest Classifier
- Decision Tree based learning
- F1 Score for evaluation

The trained model is saved using:

```python
joblib.dump(model, "rf_model.pkl")

📊 Dataset Information

The dataset contains 12,330 user sessions collected from an e-commerce website.

Features include:
Feature	Description
Administrative	Number of administrative pages visited
Informational	Number of informational pages visited
ProductRelated	Number of product pages visited
BounceRates	Bounce rate of session
ExitRates	Exit rate of session
PageValues	Value of pages visited
SpecialDay	Closeness to special shopping day
Month	Month of visit
VisitorType	Returning/New visitor
Weekend	Weekend visit indicator


🖥️ Tech Stack
Python
Streamlit
Pandas
NumPy
Scikit-learn
Joblib

* Install Dependencies : pip install -r requirements.txt

* Run Application : streamlit run app.py

📸 Application Preview
Prediction Page
User-friendly form
Feature explanations
Real-time prediction
About Page
Project overview
ML model details
Business objective
🎯 Business Goal

The objective of this project is to help businesses:

Improve customer understanding
Optimize marketing strategies
Increase conversion rates
Predict purchasing behavior
Improve revenue generation
📈 Model Evaluation

Evaluation Metric Used:

✅ F1 Score

The dataset is imbalanced, therefore F1 Score was chosen to evaluate model performance effectively.

👨‍💻 Author

Developed by: Sapam Pritamjit

📜 License

This project is for educational and learning purposes.

* Streamlit link : https://shopsmartecommerce.streamlit.app/