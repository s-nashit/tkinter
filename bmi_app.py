import streamlit as st

weight = st.number_input("Enter Weight in kgs")
height = st.number_input("Enter Height in metres")
try:
    bmi = weight/height**2
    st.write(f"Your BMI is: {bmi:.2f}")
    if bmi <18.5:
        st.warning('you are underweight')
    elif bmi>18.5 and bmi<25:
        st.success('you have a good weight')
    elif bmi>25 and bmi<30:
        st.warning('overweight')
    else:
        st.info('obesity kills')
except Exception as e:
    st.write('enter valid weight and height')

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

