import joblib
import streamlit as st
import pandas as pd


# Load the model
model = joblib.load('diabetesApp.pkl')

# Create the application
# Add app title and intro
st.set_page_config(page_title='Diabetes Prediction App', layout="centered")
st.title('Diabetes Prediction App')
st.write('Fill in the details below to predict the likelihood of diabetes')

# Create the input form
with st.form('predictionForm'):
    st.subheader('Enter Patient Data')

    # Divide into two columns
    col1, col2 = st.columns(2)

    with col1:
        # ranges are min, max, ideal/default
        pregnancies = st.slider('Pregnancies', 0, 10,step=1)
        glucose = st.slider('Glucose', 0, 200,120)
        bloodPressure = st.slider('Blood Pressure', 0, 140,70)
        bmi = st.number_input('BMI',min_value= 0.0,max_value=70.0, value=25.0)

    with col2:
        skinThickness = st.slider('Skin Thickness', 0, 100,20)
        insulin = st.slider('Insulin', 0, 900,80)
        diabetesPedigree = st.number_input('Diabetic Pedigree Function', 0.0, 2.5,0.5)
        age = st.selectbox('Age Group',options=[i for i in range(18,81,1)],index=2)

    # Submit button
    submitted = st.form_submit_button('Predict')

# Predict function
if submitted:
    inputData = pd.DataFrame([{'Pregnancies': pregnancies, 'Glucose': glucose,'BloodPressure': bloodPressure,'SkinThickness': skinThickness,
        'Insulin': insulin,'BMI': bmi,'DiabetesPedigreeFunction': diabetesPedigree,'Age': age}])
    prediction = model.predict(inputData)[0]

    if prediction == 1:
        st.error('Prediction: Positive for Diabetes')
    else:
        st.success('Prediction: Negative for Diabetes')















