import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("myfinal.pkl")  # adjust path if needed

st.title("Heart Disease Risk Predictor 💖")
st.write("Enter patient details below:")


# Chest Pain Type
chest_pain_dict = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-Anginal Pain": 2,
    "Asymptomatic": 3
}
chest_pain_type = st.selectbox("Chest Pain Type", options=list(chest_pain_dict.keys()))

# Resting ECG
resting_ecg_dict = {
    "Normal": 0,
    "ST-T wave abnormality": 1,
    "Left ventricular hypertrophy": 2
}
resting_ecg = st.selectbox("Resting ECG", options=list(resting_ecg_dict.keys()))

# ST Slope
st_slope_dict = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}
st_slope = st.selectbox("ST Slope", options=list(st_slope_dict.keys()))

# Thalassemia
thal_dict = {
    "Normal": 1,
    "Fixed Defect": 2,
    "Reversible Defect": 3
}
thalassemia = st.selectbox("Thalassemia", options=list(thal_dict.keys()))

# Exercise Angina
exercise_angina_dict = {
    "No": 0,
    "Yes": 1
}
exercise_angina = st.selectbox("Exercise Induced Angina", options=list(exercise_angina_dict.keys()))

# Fasting Blood Sugar
fbs_dict = {
    "<120 mg/dl": 0,
    ">120 mg/dl": 1
}
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar", options=list(fbs_dict.keys()))

# =======================
# Numeric inputs
# =======================
age = st.slider("Age", 1, 120, 50)
sex = st.select_slider("Sex", options=[0, 1], format_func=lambda x: "Female" if x==0 else "Male")
resting_bp = st.slider("Resting Blood Pressure", 50, 250, 120)
cholesterol = st.slider("Cholesterol", 100, 600, 200)
max_heart_rate = st.slider("Max Heart Rate", 60, 250, 150)
st_depression = st.slider("ST Depression", 0.0, 10.0, 1.0)
num_major_vessels = st.slider("Number of Major Vessels", 0, 3, 0)

# =======================
# Map selections to numeric codes for the model
# =======================
input_data = pd.DataFrame([[
    age,
    sex,
    chest_pain_dict[chest_pain_type],
    resting_bp,
    cholesterol,
    fbs_dict[fasting_blood_sugar],
    resting_ecg_dict[resting_ecg],
    max_heart_rate,
    exercise_angina_dict[exercise_angina],
    st_depression,
    st_slope_dict[st_slope],
    num_major_vessels,
    thal_dict[thalassemia]
]], columns=[
    "age", "sex", "chest_pain_type", "resting_bp", "cholesterol", "fasting_blood_sugar",
    "resting_ecg", "max_heart_rate", "exercise_angina", "st_depression",
    "st_slope", "num_major_vessels", "thalassemia"
])

# =======================
# Prediction
# =======================
if st.button("Predict Risk"):
    prediction = model.predict(input_data)[0]
    risk_label = "Low Risk" if prediction==0 else "High Risk"
    color = "green" if prediction==0 else "red"
    st.markdown(f"### Predicted Risk Level: <span style='color:{color}'>{risk_label}</span>", unsafe_allow_html=True)