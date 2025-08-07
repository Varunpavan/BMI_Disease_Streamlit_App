import streamlit as st
import numpy as np
import os
import sys

# Add error handling for model loading
try:
    from tensorflow.keras.models import load_model
    import joblib
    
    # Check if model files exist
    if not os.path.exists("model_bmi_disease.h5"):
        st.error("❌ Model file 'model_bmi_disease.h5' not found!")
        st.stop()
    
    if not os.path.exists("scaler_bmi.pkl"):
        st.error("❌ Scaler file 'scaler_bmi.pkl' not found!")
        st.stop()
    
    # Load model and scaler
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

except ImportError as e:
    st.error(f"❌ Import error: {e}")
    st.write("Please make sure all required packages are installed:")
    st.code("pip install streamlit tensorflow numpy joblib")
    
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.write("This might be due to TensorFlow compatibility issues.")
    st.write("Try running with: `TF_CPP_MIN_LOG_LEVEL=2 streamlit run app.py`")