import streamlit as st
import numpy as np

st.title("💡 Disease Risk Prediction using BMI & Deep Learning")

# Simple form inputs
age = st.slider("Age", 20, 80, 40)
bmi = st.slider("BMI", 15.0, 45.0, 25.0)
chol = st.slider("Total Cholesterol", 100, 300, 200)
bp = st.slider("Systolic Blood Pressure", 90, 200, 120)
glucose = st.slider("Glucose", 70, 200, 100)
heart_rate = st.slider("Heart Rate", 50, 120, 72)

# Simple risk calculation (placeholder)
# This is a simplified calculation for demonstration
risk_factors = []
if age > 50: risk_factors.append(20)
if bmi > 30: risk_factors.append(25)
if chol > 240: risk_factors.append(15)
if bp > 140: risk_factors.append(20)
if glucose > 126: risk_factors.append(15)
if heart_rate > 100: risk_factors.append(10)

base_risk = 10
total_risk = min(base_risk + sum(risk_factors), 100)

st.subheader("🩺 Predicted Risk:")
st.progress(total_risk)
st.write(f"**Estimated 10-year disease risk: {total_risk:.2f}%**")

if total_risk > 50:
    st.warning("⚠️ High risk! Please consult a medical professional.")
else:
    st.success("✅ Low to moderate risk. Maintain a healthy lifestyle!")

st.info("ℹ️ This is a simplified version. The full version requires TensorFlow model loading.") 