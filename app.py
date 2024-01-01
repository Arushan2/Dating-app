import streamlit as st
st.title("Mams Nivash")
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:",value=None ,min_value = 18)
sex = st.radio(
    "Select Your Sex",
    ["Male", "Female"])
Job_field = st.selectbox(
    "What is  your Job fiels",
    ('Acedamic', 'IT','Realestate Business','Local business','Sales man','Manager','Medical' ))
DOB = st.date_input("When's your birthday")