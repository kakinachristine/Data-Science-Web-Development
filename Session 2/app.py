import numpy as np
import streamlit as st
from PIL import Image
from unicodedata import category

#Display the title
st.title("BMI calculator")

# Load and display the img
image = Image.open("session2img.jpg")
st.image(image, use_container_width=True)

#Input fields: Name, height and weight
name = st.text_input("Enter your name")
weight = st.number_input("Enter your weight (in kgs)", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (in meters)", min_value=0.0, format="%.2f")


#Button and logic
if st.button("Calculate BMI"):
    if height > 0:
        # Calculate and categorise the BMI(Weight divided by the square of height)
        bmi = weight/(height**2)
        if bmi < 18.5:
            category= "Underweight"
        elif 18.5 <= bmi < 24.9:
            category= "Normal weight"
        elif 25 <= bmi < 29.9:
            category= "Overweight"
        else:
            category= "Obese"

        st.success(f"{name}, your BMI is {bmi:.2f} which is {category}.")

    else:
        st.error("Please enter a valid height.")


import pandas as pd
import numpy as np

data = pd.DataFrame({
    'BMI Range': ["Underweight", "Normal weight", "Overweight", "Obese"],
    'Min BMI':[0,18,5.25,30],
    'Max BMI':[18.5,24.9,29.9,40],
})
st.bar_chart(data[['Min BMI', 'Max BMI']])
