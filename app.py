import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="Employee Attrition", page_icon="📊", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
        /* White background */
        .stApp {
            background-color: white;
        }

        /* Default text color */
        h1, h2, h3, h4, h5, h6, p, li, span, div {
            color: #000000 !important;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #f9f9f9;
        }

        /* Blue main title */
        .custom-header {
            color: #007BFF !important;
            text-align: center;
            font-weight: 700;
            font-size: 40px;
            margin-top: 10px;
        }

        /* Section titles (like About & How it Works) */
        .section-title {
            color: #007BFF;
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 10px;
        }

        /* Body section container */
        .center-card {
            background-color: #f8faff;
            border-radius: 12px;
            padding: 25px;
            margin-top: 25px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            text-align: center;
        }

        /* Center and blue color for all h2s in cards */
        .center-card h2 {
            color: #007BFF;
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 15px;
        }

        /* Subtle animation for sections */
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(20px);}
            to {opacity: 1; transform: translateY(0);}
        }

        .fade-in {
            animation: fadeIn 1.2s ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.success("Select a page above 👆")

# --- Main Title ---
st.markdown("<h1 class='custom-header'>EMPLOYEE ATTRITION PREDICTION SYSTEM</h1>", unsafe_allow_html=True)

# --- Optional: small top illustration ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    img = Image.open('image_main.png')
    st.image(img, use_container_width=False, width=500)

# --- About the App (Centered + Blue Header) ---
st.markdown("""
<div class="center-card">
    <h2>About the app</h2>
    <p>
    Welcome to the <strong>Employee Attrition Prediction System!</strong>  
    This powerful tool helps organizations gain insights into employee turnover rates and predict potential attrition.
    </p>
    <p>
    To begin exploring your employee attrition data, simply upload your dataset or connect to your existing HR database.  
    The app will guide you through the analysis and provide step-by-step instructions on how to interpret the results.
    </p>
    <p>
    By understanding the factors that contribute to employee attrition, businesses can take proactive measures to improve
    employee retention and create a more engaged workforce.
    </p>
</div>
""", unsafe_allow_html=True)

# --- How it Works (Centered + Blue Header) ---
st.markdown("""
<div class="center-card">
    <h2>How it works</h2>
    <p>
    To begin exploring your employee attrition data, simply upload your employee information.  
    The app will predict whether the employee will continue working in the company or not.
    </p>
    <p>
    The app then processes this information and applies an advanced prediction model to provide
    an estimated employment status of the worker.
    </p>
</div>
""", unsafe_allow_html=True)

# --- Employer Section ---
st.markdown("""
<div class="center-card">
    <h2>Are you an Employer?</h2>
    <p>
    Are you an employer and you want to know if your employee will continue working with you or not?
    </p>
    <p>
    <strong style="color:#0056b3;">
    <strong>You are in the right place, you can now use our Machine Learning Model and predict the situation of your employee.</strong>
    </p>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)

