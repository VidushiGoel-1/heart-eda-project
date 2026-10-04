import streamlit as st
import pandas as pd
import joblib

# Load the saved model and everything it needs
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")
medians = joblib.load("medians.pkl")

st.title("Heart Disease Prediction")
st.write("Enter the patient details below and click Predict.")

# Inputs (one for every column in heart.csv) 
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=50)
    sex = st.selectbox("Sex", ["M", "F"])
    chest_pain = st.selectbox(
        "Chest pain type",
        ["ASY (asymptomatic)", "ATA (atypical angina)",
         "NAP (non-anginal pain)", "TA (typical angina)"])
    resting_bp = st.number_input("Resting blood pressure (mm Hg)", 0, 250, 120)
    cholesterol = st.number_input(
        "Cholesterol (mg/dl), enter 0 if unknown", 0, 700, 200)
    fasting_bs = st.selectbox(
        "Fasting blood sugar > 120 mg/dl?", [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No")

with col2:
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    max_hr = st.number_input("Maximum heart rate", 60, 220, 150)
    exercise_angina = st.selectbox(
        "Exercise-induced angina", ["N", "Y"],
        format_func=lambda x: "Yes" if x == "Y" else "No")
    oldpeak = st.number_input("Oldpeak (ST depression)", -3.0, 7.0, 0.0, step=0.1)
    st_slope = st.selectbox("ST slope", ["Up", "Flat", "Down"])

# Predict 
if st.button("Predict"):
    # Keep only the code letters (ASY, ATA, NAP, TA)
    cp = chest_pain.split(" ")[0]

    # Build one row in the same form as the training data
    row = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,
        "Sex_M": 1 if sex == "M" else 0,
        "ChestPainType_ATA": 1 if cp == "ATA" else 0,
        "ChestPainType_NAP": 1 if cp == "NAP" else 0,
        "ChestPainType_TA": 1 if cp == "TA" else 0,
        "RestingECG_Normal": 1 if resting_ecg == "Normal" else 0,
        "RestingECG_ST": 1 if resting_ecg == "ST" else 0,
        "ExerciseAngina_Y": 1 if exercise_angina == "Y" else 0,
        "ST_Slope_Flat": 1 if st_slope == "Flat" else 0,
        "ST_Slope_Up": 1 if st_slope == "Up" else 0,
    }
    input_df = pd.DataFrame([row])

    # Same cleaning as training: a 0 here means "missing" -> use the training median
    input_df["Cholesterol"] = input_df["Cholesterol"].replace(0, float("nan"))
    input_df["RestingBP"] = input_df["RestingBP"].replace(0, float("nan"))
    input_df = input_df.fillna(medians)

    # Same column order as training, then scale
    input_df = input_df[feature_columns]
    input_scaled = scaler.transform(input_df)

    # Predict
    result = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    if result == 1:
        st.error(f"The model predicts: likely a heart patient (probability {prob:.0%})")
    else:
        st.success(f"The model predicts: not likely a heart patient (probability of disease {prob:.0%})")

    st.caption("This is a student ML project, not medical advice.")