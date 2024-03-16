import sys  # Ensure sys is imported
import numpy as np
import pandas as pd
import streamlit as st
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class HealthData(BaseModel):
    age: float
    systolic_bp: float
    diastolic_bp: float
    blood_sugar: float
    body_temp: float
    heart_rate: float

@app.post("/predict")
def predict_health_risk(data: HealthData):
    # Placeholder for actual prediction logic
    return {"risk": "Example Risk"}

# Inline CSS for styling Streamlit components with requested theme
def inline_css():
    st.markdown("""
    <style>
    /* Input boxes styling */
    .stTextInput>div>div>input {
        border-radius: 20px;
        border: 2px solid #333333; /* Darker elements border */
        color: #000000; /* Black text */
        background-color: #E0E0E0; /* White background */
    }

    /* Button styling */
    .stButton>button {
        border-radius: 20px;
        color: #FFFFFF; /* White text */
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        background-color: #4CAF50; /* Green background */
        border: 2px solid #4CAF50; /* Green border */
        color: black; /* Black text */
    }

    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }

    /* Page background color */
    body {
        background-color: #FFFFFF; /* Light grey background */
    }

    /* Title and labels color */
    h1, .stLabel>label {
        color: #000000; /* Black text for title and column labels */
    }

    /* Success message styling */
    .stSuccess {
        color: #000000; /* Black text for success messages */
    }
    </style>
    """, unsafe_allow_html=True)

def st_main(): 
    st.title("Maternal Health Risk Predictor")
    inline_css()  # Apply the inline CSS for styling
    
    # Layout: Use columns to arrange inputs on a contrasting background
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age", "0")
    with col2:
        systolic_bp = st.text_input("Systolic BP", "0")
    with col3:
        diastolic_bp = st.text_input("Diastolic BP", "0")
    
    col4, col5, col6 = st.columns(3)
    with col4:
        blood_sugar = st.text_input("Blood Sugar", "0")
    with col5:
        body_temp = st.text_input("Body Temperature", "98.6")
    with col6:
        heart_rate = st.text_input("Heart Rate", "0")
    
    # Dummy Prediction Button
    if st.button("Predict"):
        st.success('Prediction: Example Risk')

if __name__ == '__main__':
    if 'streamlit' in sys.modules:
        st_main()
    else:
        # Running FastAPI app with Uvicorn programmatically
        uvicorn.run(app, host="127.0.0.1", port=8000)
