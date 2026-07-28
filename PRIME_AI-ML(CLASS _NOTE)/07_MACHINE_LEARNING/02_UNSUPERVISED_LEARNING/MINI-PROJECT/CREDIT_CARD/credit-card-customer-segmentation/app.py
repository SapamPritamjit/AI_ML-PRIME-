from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pandas as pd
import joblib

app = FastAPI(
    title="Credit Card Customer Segmentation API",
    description="Predict customer segments using KMeans clustering",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# Load Saved Models
# ==========================
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
pca = joblib.load("pca.pkl")
feature_order = joblib.load("feature_order.pkl")

# ==========================
# Pydantic Model
# ==========================
class CustomerInput(BaseModel):

    BALANCE: float = Field(..., ge=0)

    BALANCE_FREQUENCY: float = Field(..., ge=0, le=1)

    PURCHASES: float = Field(..., ge=0)

    ONEOFF_PURCHASES: float = Field(..., ge=0)

    INSTALLMENTS_PURCHASES: float = Field(..., ge=0)

    CASH_ADVANCE: float = Field(..., ge=0)

    ONEOFF_PURCHASES_FREQUENCY: float = Field(..., ge=0, le=1)

    PURCHASES_INSTALLMENTS_FREQUENCY: float = Field(..., ge=0, le=1)

    CREDIT_LIMIT: float = Field(..., gt=0)

    PAYMENTS: float = Field(..., ge=0)

    MINIMUM_PAYMENTS: float = Field(..., ge=0)

    PRC_FULL_PAYMENT: float = Field(..., ge=0, le=1)

    PURCHASES_TRX: float = Field(..., ge=0)

    CASH_ADVANCE_TRX: float = Field(..., ge=0)

    CASH_ADVANCE_FREQUENCY: float = Field(..., ge=0, le=1)

    TENURE: float = Field(..., gt=0)

# ==========================
# Cluster Information
# ==========================

CLUSTER_INFO = {
    0: {
        "name": "Premium Active Spenders",
        "description": "Customers with high spending, high credit limits and frequent purchases.",
        "recommendation": [
            "Premium Rewards Card",
            "Travel Benefits",
            "VIP Membership"
        ]
    },

    1: {
        "name": "Regular One-Off Shoppers",
        "description": "Customers who mainly make one-off purchases with moderate spending.",
        "recommendation": [
            "Cashback Offers",
            "Retail Discounts"
        ]
    },

    2: {
        "name": "Installment-Oriented Customers",
        "description": "Customers who mostly use installment purchases with relatively low balances.",
        "recommendation": [
            "Flexible Installment Plans",
            "EMI Promotions"
        ]
    },

    3: {
        "name": "Heavy Cash Advance Users",
        "description": "Customers who heavily rely on cash advances and maintain high balances.",
        "recommendation": [
            "Debt Management",
            "Balance Reduction Programs"
        ]
    },

    4: {
        "name": "Inactive / Cash Advance Dependent",
        "description": "Customers who rarely make purchases and mainly withdraw cash.",
        "recommendation": [
            "Purchase Incentives",
            "Financial Education"
        ]
    }
}

def engineer_features(data):

    purchases = data["PURCHASES"]
    payments = data["PAYMENTS"]
    balance = data["BALANCE"]
    credit_limit = data["CREDIT_LIMIT"]
    tenure = data["TENURE"]

    data["Credit_Utilization"] = balance / (credit_limit + 1)

    data["Payment_Ratio"] = payments / (balance + 1)

    data["Full_Payment_Flag"] = 1 if data["PRC_FULL_PAYMENT"] == 1 else 0

    data["ONEOFF_PURCHASES_RATIO"] = (
        data["ONEOFF_PURCHASES"] / (purchases + 1)
    )

    data["Installment_Ratio"] = (
        data["INSTALLMENTS_PURCHASES"] / (purchases + 1)
    )

    data["Case_Advance_Ratio"] = (
        data["CASH_ADVANCE"] / (credit_limit + 1)
    )

    data["Average_Pruchage_Amount"] = (
        purchases / (data["PURCHASES_TRX"] + 1)
    )

    data["Average_Case_Advance"] = (
        data["CASH_ADVANCE"] / (data["CASH_ADVANCE_TRX"] + 1)
    )

    data["Purchase_per_month"] = purchases / (tenure + 1)

    data["Payment_Per_Month"] = payments / (tenure + 1)

    data["Case_Advance_Intensity"] = (
        data["CASH_ADVANCE"] *
        data["CASH_ADVANCE_FREQUENCY"]
    )

    data["Balance_Purchase_ratio"] = (
        balance / (purchases + 1)
    )

    data["Remaining_Credit"] = (
        credit_limit - balance
    )

    data["Used_Cash_Advance"] = int(data["CASH_ADVANCE"] > 0)

    data["Used_OneOff"] = int(data["ONEOFF_PURCHASES"] > 0)

    data["Used_Installment"] = int(
        data["INSTALLMENTS_PURCHASES"] > 0
    )

    return data


# Serve CSS and JavaScript files
app.mount("/static", StaticFiles(directory="."), name="static")


@app.get("/")
async def home():
    return FileResponse("index.html")


@app.post("/predict")
async def predict(customer: CustomerInput):

    try:

        # Convert Pydantic model to dictionary
        customer = customer.model_dump()

        # Feature Engineering
        customer = engineer_features(customer)

        # Create DataFrame
        final_data = pd.DataFrame([customer])

        # Keep only features used during training
        final_data = final_data[feature_order]

        # Scale
        scaled = scaler.transform(final_data)

        # PCA
        transformed = pca.transform(scaled)

        # Predict Cluster
        cluster = int(model.predict(transformed)[0])

        # Get Cluster Information
        info = CLUSTER_INFO[cluster]

        return {

            "success": True,

            "cluster": cluster,

            "segment": info["name"],

            "description": info["description"],

            "recommendation": info["recommendation"],

            "metrics": {

                "Credit Utilization": round(customer["Credit_Utilization"], 3),

                "Payment Ratio": round(customer["Payment_Ratio"], 3),

                "Remaining Credit": round(customer["Remaining_Credit"], 2),

                "Purchase per Month": round(customer["Purchase_per_month"], 2),

                "Average Purchase": round(customer["Average_Pruchage_Amount"], 2)

            }

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }