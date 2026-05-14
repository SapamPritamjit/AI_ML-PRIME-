# app.py

import streamlit as st
import pandas as pd
import joblib
import os

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="ShopSmart Analytics",
    page_icon="🛒",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "rf_model.pkl")

model = joblib.load(MODEL_PATH)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(to right, #050816, #0b1023);
    color: white;
}

/* TITLE */
.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: bold;
    color: #6C63FF;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: #cfcfcf;
    font-size: 18px;
    margin-bottom: 40px;
}

/* CARD */
.card {
    background-color: #111827;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 0px 25px rgba(108, 99, 255, 0.2);
    margin-bottom: 20px;
}

/* ABOUT BOX */
.about-box {
    background-color: white;
    color: black;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0px 0px 25px rgba(255,255,255,0.08);
    line-height: 1.8;
}

.about-box h2 {
    color: #6C63FF;
    margin-bottom: 20px;
}

.about-box p {
    color: #222;
    font-size: 17px;
}

.about-box li {
    color: #222;
    font-size: 17px;
    margin-bottom: 8px;
}

/* BUTTON */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #6C63FF, #8B5CF6);
    color: white;
    font-size: 20px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    height: 55px;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #5A52E8, #7C3AED);
    color: white;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #1b1f2e;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# FEATURE HELP TEXT
# ==========================================

feature_help = {
    "Administrative": "Number of administrative pages visited (login, account, settings).",
    "Administrative_Duration": "Time spent on administrative pages in seconds.",
    "Informational": "Number of informational pages visited.",
    "Informational_Duration": "Time spent on informational pages in seconds.",
    "ProductRelated": "Number of product-related pages visited.",
    "ProductRelated_Duration": "Time spent on product-related pages.",
    "BounceRates": "Percentage of visitors leaving after viewing one page.",
    "ExitRates": "Percentage of exits from pages.",
    "PageValues": "Average value of pages before completing purchase.",
    "SpecialDay": "Closeness to a special shopping day.",
    "Month": "Month of visit.",
    "OperatingSystems": "Operating system used by visitor.",
    "Browser": "Browser used by visitor.",
    "Region": "Visitor geographic region.",
    "TrafficType": "Traffic source type.",
    "VisitorType": "Returning or new visitor.",
    "Weekend": "Whether visit happened on weekend."
}

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🗂 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Prediction", "About Website"]
)

# ==========================================
# ABOUT PAGE
# ==========================================

if page == "About Website":

    st.markdown(
        "<div class='main-title'>🛒 ShopSmart Analytics</div>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class='about-box'>

    <h2>📌 About This Project</h2>

    <p>
    This machine learning application predicts whether a visitor is likely
    to purchase a product from an e-commerce website.
    </p>

    <p>
    The model analyzes user browsing behavior including:
    </p>

    <ul>
        <li>Pages visited</li>
        <li>Time spent on website</li>
        <li>Traffic source</li>
        <li>Visitor type</li>
        <li>Bounce rates</li>
        <li>Exit rates</li>
        <li>Product interactions</li>
    </ul>

    <h2>🤖 Machine Learning Model</h2>

    <p>
    Multiple machine learning algorithms were trained and evaluated.
    </p>

    <p>
    ✅ Best Model: <b>Random Forest Classifier</b>
    </p>

    <p>
    📊 Evaluation Metric: <b>F1 Score</b>
    </p>

    <h2>🎯 Goal</h2>

    <p>
    Help businesses improve:
    </p>

    <ul>
        <li>Customer understanding</li>
        <li>Marketing strategy</li>
        <li>Sales conversion</li>
        <li>Revenue optimization</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

# ==========================================
# PREDICTION PAGE
# ==========================================

else:

    st.markdown(
        "<div class='main-title'>🛒 ShopSmart Analytics</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Predict whether a visitor will complete a purchase</div>",
        unsafe_allow_html=True
    )

    with st.container():

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        # ==========================================
        # LEFT COLUMN
        # ==========================================

        with col1:

            Administrative = st.number_input(
                "Administrative",
                min_value=0,
                value=2,
                help=feature_help["Administrative"]
            )

            Administrative_Duration = st.number_input(
                "Administrative Duration",
                min_value=0.0,
                value=50.0,
                help=feature_help["Administrative_Duration"]
            )

            Informational = st.number_input(
                "Informational",
                min_value=0,
                value=1,
                help=feature_help["Informational"]
            )

            Informational_Duration = st.number_input(
                "Informational Duration",
                min_value=0.0,
                value=20.0,
                help=feature_help["Informational_Duration"]
            )

            ProductRelated = st.number_input(
                "Product Related",
                min_value=0,
                value=20,
                help=feature_help["ProductRelated"]
            )

            ProductRelated_Duration = st.number_input(
                "Product Related Duration",
                min_value=0.0,
                value=300.0,
                help=feature_help["ProductRelated_Duration"]
            )

            BounceRates = st.slider(
                "Bounce Rates",
                0.0,
                1.0,
                0.02,
                help=feature_help["BounceRates"]
            )

            ExitRates = st.slider(
                "Exit Rates",
                0.0,
                1.0,
                0.05,
                help=feature_help["ExitRates"]
            )

            PageValues = st.number_input(
                "Page Values",
                min_value=0.0,
                value=5.0,
                help=feature_help["PageValues"]
            )

        # ==========================================
        # RIGHT COLUMN
        # ==========================================

        with col2:

            SpecialDay = st.selectbox(
                "Special Day",
                [0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
                help=feature_help["SpecialDay"]
            )

            Month = st.selectbox(
                "Month",
                ['Feb', 'Mar', 'May', 'June', 'Jul', 'Sep', 'Oct', 'Nov', 'Dec'],
                help=feature_help["Month"]
            )

            OperatingSystems = st.selectbox(
                "Operating Systems",
                [1,2,3,4,5,6,7,8],
                help=feature_help["OperatingSystems"]
            )

            Browser = st.selectbox(
                "Browser",
                [1,2,3,4,5,6,7,8,9,10,11,12,13],
                help=feature_help["Browser"]
            )

            Region = st.selectbox(
                "Region",
                [1,2,3,4,5,6,7,8,9],
                help=feature_help["Region"]
            )

            TrafficType = st.selectbox(
                "Traffic Type",
                list(range(1, 21)),
                help=feature_help["TrafficType"]
            )

            VisitorType = st.selectbox(
                "Visitor Type",
                ['Returning_Visitor', 'New_Visitor', 'Other'],
                help=feature_help["VisitorType"]
            )

            Weekend = st.selectbox(
                "Weekend",
                [False, True],
                help=feature_help["Weekend"]
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # PREDICTION
    # ==========================================

    if st.button("🔮 Predict Purchase"):

        # VisitorType Encoding
        visitor_mapping = {
            'Returning_Visitor': 2,
            'New_Visitor': 1,
            'Other': 0
        }

        VisitorType = visitor_mapping[VisitorType]

        # Base Data
        input_data = pd.DataFrame({
            'Administrative': [Administrative],
            'Administrative_Duration': [Administrative_Duration],
            'Informational': [Informational],
            'Informational_Duration': [Informational_Duration],
            'ProductRelated': [ProductRelated],
            'ProductRelated_Duration': [ProductRelated_Duration],
            'BounceRates': [BounceRates],
            'ExitRates': [ExitRates],
            'PageValues': [PageValues],
            'SpecialDay': [SpecialDay],
            'OperatingSystems': [OperatingSystems],
            'Browser': [Browser],
            'Region': [Region],
            'TrafficType': [TrafficType],
            'VisitorType': [VisitorType]
        })

        # ==========================================
        # MONTH ENCODING
        # ==========================================

        month_columns = [
            'Month_Dec',
            'Month_Feb',
            'Month_Jul',
            'Month_June',
            'Month_Mar',
            'Month_May',
            'Month_Nov',
            'Month_Oct',
            'Month_Sep'
        ]

        for col in month_columns:
            input_data[col] = 0

        month_mapping = {
            'Dec': 'Month_Dec',
            'Feb': 'Month_Feb',
            'Jul': 'Month_Jul',
            'June': 'Month_June',
            'Mar': 'Month_Mar',
            'May': 'Month_May',
            'Nov': 'Month_Nov',
            'Oct': 'Month_Oct',
            'Sep': 'Month_Sep'
        }

        if Month in month_mapping:
            input_data[month_mapping[Month]] = 1

        # ==========================================
        # WEEKEND ENCODING
        # ==========================================

        input_data['Weekend'] = Weekend
        input_data['weekend'] = 1 if Weekend else 0

        # ==========================================
        # FINAL COLUMN ORDER
        # ==========================================

        final_columns = [
            'Administrative',
            'Administrative_Duration',
            'Informational',
            'Informational_Duration',
            'ProductRelated',
            'ProductRelated_Duration',
            'BounceRates',
            'ExitRates',
            'PageValues',
            'SpecialDay',
            'OperatingSystems',
            'Browser',
            'Region',
            'TrafficType',
            'VisitorType',
            'Weekend',
            'Month_Dec',
            'Month_Feb',
            'Month_Jul',
            'Month_June',
            'Month_Mar',
            'Month_May',
            'Month_Nov',
            'Month_Oct',
            'Month_Sep',
            'weekend'
        ]

        input_data = input_data[final_columns]

        # ==========================================
        # PREDICTION
        # ==========================================

        prediction = model.predict(input_data)[0]

        st.markdown("<br>", unsafe_allow_html=True)

        if prediction == 1 or prediction == True:

            st.success("✅ This visitor is LIKELY to make a purchase!")

            st.balloons()

        else:

            st.error("❌ This visitor is NOT likely to make a purchase.")