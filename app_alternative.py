import streamlit as st
import numpy as np
import os

st.title("💡 Disease Risk Prediction using BMI & Deep Learning")

# Try to load TensorFlow model, fall back to simple calculation if it fails
model_loaded = False
scaler_loaded = False

try:
    from tensorflow.keras.models import load_model
    import joblib
    
    # Check if model files exist
    if os.path.exists("model_bmi_disease.h5") and os.path.exists("scaler_bmi.pkl"):
        model = load_model("model_bmi_disease.h5")
        scaler = joblib.load("scaler_bmi.pkl")
        model_loaded = True
        scaler_loaded = True
        st.success("✅ TensorFlow model loaded successfully!")
    else:
        st.warning("⚠️ Model files not found, using simplified calculation.")
        
except Exception as e:
    st.warning(f"⚠️ TensorFlow model loading failed: {str(e)[:100]}...")
    st.info("Using simplified risk calculation instead.")

# Form inputs
age = st.slider("Age", 20, 80, 40)
bmi = st.slider("BMI", 15.0, 45.0, 25.0)
chol = st.slider("Total Cholesterol", 100, 300, 200)
bp = st.slider("Systolic Blood Pressure", 90, 200, 120)
glucose = st.slider("Glucose", 70, 200, 100)
heart_rate = st.slider("Heart Rate", 50, 120, 72)

# Calculate risk
if model_loaded and scaler_loaded:
    try:
        input_data = np.array([[age, bmi, chol, bp, glucose, heart_rate]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0][0]
        risk_percent = prediction * 100
        st.success("🎯 Using TensorFlow model prediction")
    except Exception as e:
        st.error(f"Model prediction failed: {str(e)}")
        risk_percent = 0
else:
    # Simple risk calculation as fallback
    risk_factors = []
    if age > 50: risk_factors.append(20)
    if bmi > 30: risk_factors.append(25)
    if chol > 240: risk_factors.append(15)
    if bp > 140: risk_factors.append(20)
    if glucose > 126: risk_factors.append(15)
    if heart_rate > 100: risk_factors.append(10)
    
    base_risk = 10
    risk_percent = min(base_risk + sum(risk_factors), 100)
    st.info("📊 Using simplified risk calculation")

st.subheader("🩺 Predicted Risk:")
st.progress(min(int(risk_percent), 100))
st.write(f"**Estimated 10-year disease risk: {risk_percent:.2f}%**")

if risk_percent > 50:
    st.warning("⚠️ High risk! Please consult a medical professional.")
else:
    st.success("✅ Low to moderate risk. Maintain a healthy lifestyle!")

# Additional information
st.markdown("---")
st.markdown("### 📋 Risk Factors Considered:")
st.markdown("- **Age**: Higher risk for ages > 50")
st.markdown("- **BMI**: Higher risk for BMI > 30 (obese)")
st.markdown("- **Cholesterol**: Higher risk for levels > 240 mg/dL")
st.markdown("- **Blood Pressure**: Higher risk for systolic > 140 mmHg")
st.markdown("- **Glucose**: Higher risk for levels > 126 mg/dL")
st.markdown("- **Heart Rate**: Higher risk for rates > 100 bpm") 