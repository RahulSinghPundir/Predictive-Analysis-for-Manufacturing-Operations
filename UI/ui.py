# Import required libraries
import streamlit as st
import requests
import pandas as pd
import numpy as np
import pickle as pkl
import subprocess

# API Base URL
BASE_URL = "http://127.0.0.1:5000"  # Replace with your API base URL

# Set up the main application title and sidebar
st.title("Manufacturing Operations - Predictive Analysis")
st.sidebar.header("API Endpoints")

# Create navigation options in sidebar
options = ["Upload Data", "Train Model", "Make Prediction"]
choice = st.sidebar.selectbox("Choose Action", options)



# Handle data upload functionality
if choice == "Upload Data":
    st.header("Upload Manufacturing Data")
     # Create file uploader widget that accepts only CSV files
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    if uploaded_file:
        # Read and preprocess uploaded CSV file
        data = pd.read_csv(uploaded_file)
        # Remove auto-generated index column if present
        if('Unnamed: 0' in data.columns):
            data.drop("Unnamed: 0", axis=1, inplace=True)
        # Display preview of uploaded data
        st.write("Uploaded Data Preview:")
        st.dataframe(data)
        # Save data when upload button is clicked
        if st.button("Upload Data"):
            data.to_csv("data.csv")
            st.success("Data Uploaded Successfully!")

# Handle model training functionality
elif choice == "Train Model":
    st.header("Train the Model")
    # Execute model training script when button is clicked
    if st.button("Train Model"):
        subprocess.run(["python", "model_run.py"])
        st.success("Model Trained Successfully!")
        
        

# Prediction interface section
elif choice == "Make Prediction":
    # Collect numerical inputs for machine parameters
    hydraulic_pressure = st.number_input("Hydraulic Pressure (bar)", min_value=0.0, step=0.1)
    spindle_speed = st.number_input("Spindle Speed (RPM)", min_value=0, step=1)
    torque = st.number_input("Torque (Nm)", min_value=0.0, step=0.1)
    cutting = st.number_input("Cutting (kN)", min_value=0.0, step=0.1)
    
    # Create dictionary with input parameters
    input_data = {
        "Hydraulic_Pressure(bar)": hydraulic_pressure,
        "Spindle_Speed(RPM)": spindle_speed,
        "Torque(Nm)": torque,
        "Cutting(kN)": cutting
    }
    
    # Convert input data to DataFrame format for model prediction
    df=pd.DataFrame(input_data,index=[0])
    
    # Load the trained model from disk
    with open('model.pkl', 'rb') as file:
        model = pkl.load(file)
    
    # Make prediction using loaded model
    result = model.predict(df)[0]
    
    st.header("Make Prediction")
    
    # Display prediction results when button is clicked
    if st.button("Make Prediction"):
        if result:
            st.error(f"Downtime Failure with result")  # Show error message for predicted failure
        else:
            st.success(f"Success with result")         # Show success message for normal operation


