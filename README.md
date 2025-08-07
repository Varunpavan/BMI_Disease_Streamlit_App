# 🏥 BMI Disease Risk Prediction App

A Streamlit-based web application that predicts 10-year disease risk using health parameters and machine learning.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Risk Factors](#risk-factors)
- [Troubleshooting](#troubleshooting)
- [Medical Disclaimer](#medical-disclaimer)

## 🎯 Overview

This application provides an interactive interface for predicting disease risk based on key health metrics. It uses either a trained TensorFlow neural network model or a rule-based calculation system to assess 10-year disease risk.

**Current Status**: ✅ **Running Successfully**
- **Local URL**: http://localhost:8501
- **Network URL**: http://192.168.0.108:8501

## ✨ Features

- **Interactive Health Assessment**: Real-time risk calculation as you adjust parameters
- **Multiple Input Parameters**: Age, BMI, Cholesterol, Blood Pressure, Glucose, Heart Rate
- **Visual Risk Display**: Progress bar and percentage-based risk assessment
- **Medical Guidance**: Automated advice based on risk level
- **Responsive Design**: Works on desktop and mobile devices
- **Error Handling**: Graceful fallback when ML model is unavailable

## 📁 Project Structure

```
BMI_Disease_Streamlit_App/
├── app.py                    # Original app with TensorFlow model
├── app_simple.py            # Simplified version (currently running)
├── app_alternative.py       # Alternative with fallback logic
├── model_bmi_disease.h5     # Trained TensorFlow model
├── scaler_bmi.pkl          # Data scaler for normalization
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone or download the project**
   ```bash
   cd BMI_Disease_Streamlit_App
   ```

2. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   # For simplified version (recommended)
   streamlit run app_simple.py
   
   # For original version (may have TensorFlow issues)
   streamlit run app.py
   
   # For alternative version with fallback
   streamlit run app_alternative.py
   ```

## 💻 Usage

### How to Use the App

1. **Open your browser** and navigate to http://localhost:8501
2. **Adjust the sliders** to match your health metrics:
   - **Age**: 20-80 years
   - **BMI**: 15.0-45.0 (Body Mass Index)
   - **Total Cholesterol**: 100-300 mg/dL
   - **Systolic Blood Pressure**: 90-200 mmHg
   - **Glucose**: 70-200 mg/dL
   - **Heart Rate**: 50-120 bpm

3. **View real-time results**:
   - Risk percentage display
   - Visual progress bar
   - Medical advice based on risk level

4. **Interpret results**:
   - **Low to Moderate Risk** (<50%): Maintain healthy lifestyle
   - **High Risk** (>50%): Consult medical professional

### Example Usage

```
Input Parameters:
- Age: 45 years
- BMI: 28.5
- Cholesterol: 220 mg/dL
- Blood Pressure: 135 mmHg
- Glucose: 95 mg/dL
- Heart Rate: 75 bpm

Result: 35% risk (Low to moderate risk)
```

## 🔧 Technical Details

### Machine Learning Model

**Original App (`app.py`)**:
- **Framework**: TensorFlow/Keras
- **Model Type**: Neural Network
- **Input**: 6 health parameters
- **Output**: Risk probability (0-1)
- **Data Processing**: StandardScaler normalization

**Simplified App (`app_simple.py`)**:
- **Method**: Rule-based calculation
- **Logic**: Risk factor accumulation
- **Advantage**: No TensorFlow dependency

### Risk Calculation Logic

```python
# Simplified version logic
risk_factors = []
if age > 50: risk_factors.append(20)        # Age risk
if bmi > 30: risk_factors.append(25)        # Obesity risk
if chol > 240: risk_factors.append(15)      # High cholesterol
if bp > 140: risk_factors.append(20)        # High blood pressure
if glucose > 126: risk_factors.append(15)   # High glucose
if heart_rate > 100: risk_factors.append(10) # High heart rate

base_risk = 10
total_risk = min(base_risk + sum(risk_factors), 100)
```

## 📊 Risk Factors

| Health Parameter | Normal Range | High Risk Threshold | Medical Significance |
|------------------|-------------|-------------------|-------------------|
| **Age** | 20-80 years | >50 years | Increased risk with age |
| **BMI** | 18.5-24.9 | >30 (Obese) | Obesity-related diseases |
| **Cholesterol** | <200 mg/dL | >240 mg/dL | Cardiovascular disease risk |
| **Blood Pressure** | <120/80 | >140/90 | Hypertension risk |
| **Glucose** | 70-100 mg/dL | >126 mg/dL | Diabetes risk |
| **Heart Rate** | 60-100 bpm | >100 bpm | Cardiovascular stress |

## 🔧 Troubleshooting

### Common Issues

#### 1. TensorFlow Compatibility Issues
**Problem**: App crashes with mutex lock errors
```
libc++abi: terminating due to uncaught exception of type std::__1::system_error: mutex lock failed: Invalid argument
```

**Solution**: Use the simplified version
```bash
streamlit run app_simple.py
```

#### 2. Port Already in Use
**Problem**: Port 8501 is occupied
**Solution**: Use a different port
```bash
streamlit run app_simple.py --server.port 8502
```

#### 3. Missing Dependencies
**Problem**: Import errors
**Solution**: Reinstall dependencies
```bash
pip3 install -r requirements.txt
```

### Environment Variables

For TensorFlow compatibility, try:
```bash
TF_CPP_MIN_LOG_LEVEL=2 streamlit run app.py
```

## ⚠️ Medical Disclaimer

**IMPORTANT**: This application is for **educational and demonstration purposes only**.

- ❌ **NOT for medical diagnosis**
- ❌ **NOT for treatment decisions**
- ❌ **NOT a substitute for professional medical advice**

**Always consult qualified healthcare professionals for:**
- Medical diagnosis
- Treatment decisions
- Health assessments
- Risk evaluations

## 🛠️ Development

### Adding New Features

1. **Additional Health Parameters**:
   - Smoking status
   - Family history
   - Physical activity level
   - Diet patterns

2. **Enhanced Risk Calculation**:
   - More sophisticated algorithms
   - Multiple disease types
   - Age-specific risk factors

3. **User Interface Improvements**:
   - Data visualization
   - Risk trend analysis
   - Export functionality

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📈 Future Enhancements

- [ ] Fix TensorFlow compatibility issues
- [ ] Add more health parameters
- [ ] Implement user authentication
- [ ] Add data export functionality
- [ ] Include detailed risk explanations
- [ ] Add multiple disease type predictions
- [ ] Implement data validation
- [ ] Add mobile app version

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure all dependencies are installed
3. Try the simplified version (`app_simple.py`)
4. Check Python version compatibility

## 📄 License

This project is for educational purposes. Please ensure compliance with local regulations when using health-related applications.

---

**Last Updated**: January 2025  
**Version**: 1.0.0  
**Status**: ✅ Running Successfully