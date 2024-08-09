import streamlit as st
# Use Streamlit's column layout for better alignment and control
col1, col2 = st.columns([1, 20])

with col2:
    # Display the author details
    st.markdown("""
        ### Bonny Makuwa
        **Topics:** Machine Learning, Data Analysis, Predictive Modeling, Power Bi , Python, SQL    
        **Biography:** Focused on predictive modeling and data analysis. Proficient in Power BI, Python, SQL, and machine learning techniques. Experienced in creating and optimizing models to drive insights and enhance decision-making processes.
    """)

# Custom CSS to change the color scheme to grey
st.markdown("""
    <style>
        .main {
            background-color: #f0f0f0;
            color: ##333;
        }
        .stButton button {
            background-color: #666666;
            color: #ffffff;
        }
        .stSelectbox, .stSlider {
            color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

# Publication info displayed separately
st.markdown("""
<div style="text-align: center;">
    <h2>Linkedin and Github</h2>
    <p><a href="https://www.linkedin.com/in/bonny-makuwa-04a8b6153/">https://www.linkedin.com/in/bonny-makuwa-04a8b6153/</a></p>
    <p><a href="https://https://github.com/Bonnymakuwa/">https://github.com/Bonnymakuwa</a></p>
</div>
""", unsafe_allow_html=True)

st.title('Heart Disease Prediction Model')

st.write("""
## Model Description
This heart disease prediction model is developed to help evaluate the likelihood of heart disease based on various health parameters. It uses commonly recognized thresholds to assess risk levels and provide insights based on user inputs.
""")

# User input for heart disease prediction
age = st.slider('**Age**', 0, 120, 30)
sex = st.selectbox('**Sex**', ['Female', 'Male'])
chest_pain = st.selectbox('**Chest Pain Type**', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
resting_blood_pressure = st.slider('**Resting Blood Pressure (mm Hg)**', 0, 200, 120)
cholesterol = st.slider('**Cholesterol (mg/dl)**', 0, 600, 200)
fasting_blood_sugar = st.selectbox('**Fasting Blood Sugar ≥ 120 mg/dl**', ['No', 'Yes'])
resting_electrocardiographic_results = st.selectbox('**Resting Electrocardiographic Results**', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
max_heart_rate = st.slider('**Maximum Heart Rate Achieved (bpm)**', 0, 250, 150)
exercise_induced_angina = st.selectbox('**Exercise Induced Angina**', ['No', 'Yes'])

# Prediction logic
def predict_disease(age, sex, chest_pain, resting_blood_pressure, cholesterol, fasting_blood_sugar, resting_electrocardiographic_results, max_heart_rate, exercise_induced_angina):
    risk_score = 0
    
    # Age
    if age >= 65:
        risk_score += 2
    elif age >= 45:
        risk_score += 1
    
    # Sex
    if sex == 'Male':
        risk_score += 2
    
    # Chest Pain Type
    if chest_pain == 'Typical Angina':
        risk_score += 3
    elif chest_pain == 'Atypical Angina':
        risk_score += 2
    elif chest_pain == 'Non-anginal Pain':
        risk_score += 1
    
    # Resting Blood Pressure
    if resting_blood_pressure >= 140:
        risk_score += 2
    elif resting_blood_pressure >= 120:
        risk_score += 1
    
    # Cholesterol
    if cholesterol >= 240:
        risk_score += 2
    elif cholesterol >= 200:
        risk_score += 1
    
    # Fasting Blood Sugar
    if fasting_blood_sugar == 'Yes':
        risk_score += 2
    
    # Resting Electrocardiographic Results
    if resting_electrocardiographic_results == 'Left Ventricular Hypertrophy':
        risk_score += 3
    elif resting_electrocardiographic_results == 'ST-T Wave Abnormality':
        risk_score += 2
    
    # Maximum Heart Rate Achieved
    if max_heart_rate < 120:
        risk_score += 2
    elif max_heart_rate < 160:
        risk_score += 1
    
    # Exercise-Induced Angina
    if exercise_induced_angina == 'Yes':
        risk_score += 2

    # Risk assessment based on score
    if risk_score >= 10:
        return "High risk of heart disease"
    elif risk_score >= 5:
        return "Moderate risk of heart disease"
    else:
        return "Low risk of heart disease"

# Predict disease
prediction = predict_disease(
    age,
    sex,
    chest_pain,
    resting_blood_pressure,
    cholesterol,
    fasting_blood_sugar,
    resting_electrocardiographic_results,
    max_heart_rate,
    exercise_induced_angina
)

# Display results with increased emphasis
st.markdown(f"""
### **Prediction**
**{prediction}**
""", unsafe_allow_html=True)
