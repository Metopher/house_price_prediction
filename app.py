import streamlit as st
import joblib
import numpy as np
import os
import time

def local_css(file_name):
    try:
        css_path = os.path.join(os.path.dirname(__file__), file_name)
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Could not find the stylesheet: {file_name}. Please ensure it is in the same directory.")
    except Exception as e:
        st.error(f"An error occurred while loading CSS: {e}")

st.set_page_config(
    page_title="House Price Prediction",
    layout="centered"
)

local_css("style.css")

# Load Model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    model = None

# --- Main Content ---
# Note: We removed the 'main-card' HTML wrapper. 
# The card styling is now applied to the whole container in CSS.

# Header Section
st.markdown('<div class="app-title">Real Estate Estimator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">AI-powered valuation based on property specifications.</div>',
    unsafe_allow_html=True
)

# Input Section
st.markdown('<div class="section-title">Property Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    bedrooms = st.number_input("Bedrooms", min_value=0, value=3, step=1)
    bathrooms = st.number_input("Bathrooms", min_value=0, value=2, step=1)
    condition = st.number_input("Condition (1-5)", min_value=1, max_value=5, value=3, step=1)

with col2:
    livingarea = st.number_input("Living Area (sq ft)", min_value=100, value=2500, step=100)
    numberofschools = st.number_input("Nearby Schools", min_value=0, value=1, step=1)

# Prediction Section
st.markdown('<div class="section-title">Valuation</div>', unsafe_allow_html=True)

X = [bedrooms, bathrooms, livingarea, condition, numberofschools]

predictbutton = st.button("Calculate Value")

if predictbutton:
    if model is not None:
        with st.spinner('Analyzing market data...'):
            time.sleep(0.5) 
            X_array = np.array(X).reshape(1, -1)
            prediction = model.predict(X_array)[0]

        st.markdown(
            f"""
            <div class="prediction-box">
                <div class="prediction-label">Estimated Market Value</div>
                <div class="prediction-value">₹{prediction:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("⚠️ Model file not found. Please ensure 'model.pkl' is in the directory.")
else:
    st.markdown(
        '<div class="helper-text">Adjust the parameters above and click <b>Calculate Value</b> to generate an estimate.</div>',
        unsafe_allow_html=True
    )