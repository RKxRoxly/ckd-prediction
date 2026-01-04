import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="CKD Prediction", layout="centered")

with st.sidebar:
    st.header("Project Submission")
    st.info("**Domain:** AI in Healthcare")
    st.write("**Name:** Santanu Das")
    st.write("**Algorithm:** Logistic Regression")
    

st.title("Chronic Kidney Disease Prediction ")
st.markdown("##### AI-powered screening tool for early detection of kidney risk.")
st.divider()

try:
    with open('ckd_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file 'ckd_model.pkl' not found.")
    st.stop()

st.subheader("Clinical Parameters")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Patient Age", 1, 100, 45)
    bp = st.number_input("Blood Pressure (Diastolic)", 50, 180, 80)
    sg = st.number_input("Specific Gravity (1.005-1.025)", 1.005, 1.025, 1.020, format="%.3f")
    al = st.number_input("Albumin Level (0-5)", 0, 5, 0)

with col2:
    bgr = st.number_input("Blood Glucose Random (mgs/dl)", 50, 500, 120)
    sc = st.number_input("Serum Creatinine (0.4-15.0)", 0.4, 15.0, 1.2)
    hemo = st.number_input("Hemoglobin (3-18)", 3.0, 18.0, 15.0)

st.divider()

if st.button("Generate Diagnostic Report"):
    features = np.array([[age, bp, sg, al, bgr, sc, hemo]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("### Result: High Risk of CKD Detected ⚠️")
        st.warning("Recommendation: Clinical metrics suggest potential kidney issues. Please consult a nephrologist.")
    else:
        st.success("### Result: Low Risk (Healthy Kidney Function) ✅")
        st.info("The clinical metrics provided are within the normal range for kidney function.")
