import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
import joblib

model = load_model("model_bmi_disease.h5")
scaler = joblib.load("scaler_bmi.pkl")

st.title("💡 Disease Risk Prediction using BMI & Deep Learning")

age = st.slider("Age", 20, 80, 40)
bmi = st.slider("BMI", 15.0, 45.0, 25.0)
chol = st.slider("Total Cholesterol", 100, 300, 200)
bp = st.slider("Systolic Blood Pressure", 90, 200, 120)
glucose = st.slider("Glucose", 70, 200, 100)
heart_rate = st.slider("Heart Rate", 50, 120, 72)

input_data = np.array([[age, bmi, chol, bp, glucose, heart_rate]])
input_scaled = scaler.transform(input_data)
prediction = model.predict(input_scaled)[0][0]
risk_percent = prediction * 100

st.subheader("🩺 Predicted Risk:")
st.progress(min(int(risk_percent), 100))
st.write(f"**Estimated 10-year disease risk: {risk_percent:.2f}%**")

if risk_percent > 50:
    st.warning("⚠️ High risk! Please consult a medical professional.")
else:
    st.success("✅ Low to moderate risk. Maintain a healthy lifestyle!")