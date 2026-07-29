# 💳 Credit Card Customer Segmentation

A Machine Learning web application that segments credit card customers into different groups based on their financial behavior using **K-Means Clustering**. The project provides an interactive dashboard where users can enter customer information and receive the predicted customer segment along with insights and recommendations.

---

## 📌 Features

- Customer segmentation using K-Means Clustering
- PCA for dimensionality reduction
- Feature engineering pipeline
- Data preprocessing using StandardScaler
- Interactive dashboard
- Financial metrics visualization
- Customer segment descriptions
- Personalized recommendations
- Input help tooltips for all features
- FastAPI backend
- HTML, CSS and JavaScript frontend

---

## 🛠️ Technologies Used

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- K-Means Clustering
- PCA
- StandardScaler
- Joblib

### Backend

- FastAPI
- Uvicorn
- Pydantic

### Frontend

- HTML5
- CSS3
- JavaScript
- Chart.js

---

## 📂 Project Structure

```text
credit-card-customer-segmentation/
│
├── app.py
├── index.html
├── style.css
├── script.js
│
├── model.pkl
├── scaler.pkl
├── pca.pkl
├── feature_order.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd credit-card-customer-segmentation
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Backend

Start the FastAPI server

```bash
uvicorn app:app --reload
```

The backend will run at

```
http://127.0.0.1:8000
```

---

# 💻 Run the Frontend

Since the frontend is built using HTML, CSS and JavaScript, simply open

```
index.html
```

using

- Live Server (VS Code Recommended)

or

- Any modern web browser

If using VS Code:

1. Install the **Live Server** extension.
2. Right-click `index.html`.
3. Select **Open with Live Server**.

The frontend usually runs at

```
http://127.0.0.1:5500
```

---

# 🔗 Backend API

Prediction Endpoint

```
POST /predict
```

Example

```
http://127.0.0.1:8000/predict
```

---

# 📊 Machine Learning Pipeline

```
Input Data
      │
      ▼
Feature Engineering
      │
      ▼
StandardScaler
      │
      ▼
PCA
      │
      ▼
K-Means Model
      │
      ▼
Customer Segment
```

---

# 📈 Customer Segments

- Premium Active Spenders
- Regular One-Off Shoppers
- Installment-Oriented Customers
- Heavy Cash Advance Users
- Inactive / Cash Advance Dependent

---

# 📸 Screenshots

Add screenshots of

- Dashboard
- Prediction Result
- Charts
- Recommendations

---

# 🚀 Future Improvements

- Deploy backend on Render
- Deploy frontend on Render Static Site
- User authentication
- Customer history
- Export prediction report
- Dark mode

---

# 👨‍💻 Author

**Sapam Pritamjit**