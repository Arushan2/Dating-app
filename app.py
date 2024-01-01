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
user_image = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])
if user_image is not None:
    st.image(user_image, caption="Uploaded Image", use_column_width=True)
Email = st.text_input("Enter your E-Mail address")
password = st.text_input("Create your password", type="password")
confirm_password = st.text_input("Re-enter your password", type="password")

if (password != confirm_password):
    st.error("Passwords do not match. Please re-enter matching passwords.")
else:
    st.success("Passwords match!")
    st.button("Submit")

