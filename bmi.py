import streamlit as st
st.title("BMI Calculator")

weight = st.number_input("Enter your Weight in KG", step = 0.1)
height = st.number_input("Enter your Height in Meters")
bmi = weight/(height)**2
st.success(f"Your BMI is {bmi}")
if weight > 0 and height > 0:
    st.write(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
else:
    st.write("Please enter valid weight and height.")


