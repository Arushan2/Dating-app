import streamlit as st
import json

st.title("Mams Nivash")

# User information inputs
name = st.text_input("Enter your name:", required=True)
age = st.number_input("Enter your age:", value=None, min_value=18, required=True)
sex = st.radio("Select Your Sex", ["Male", "Female"], required=True)
job_field = st.selectbox("What is your Job field", ('Academic', 'IT', 'Real Estate Business', 'Local Business', 'Salesman', 'Manager', 'Medical'), required=True)
dob = st.date_input("When's your birthday", required=True)

# Upload user image
user_image = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

# Email and Password
email = st.text_input("Enter your E-Mail address", required=True)
password = st.text_input("Create your password", type="password", required=True)
confirm_password = st.text_input("Re-enter your password", type="password", required=True)

# Check if passwords match
passwords_match = password == confirm_password

# Submit button
if st.button("Submit"):
    if not passwords_match:
        st.error("Passwords do not match. Please re-enter matching passwords.")
    else:
        # Store user data in separate JSON files
        user_data = {
            "name": name,
            "age": age,
            "sex": sex,
            "job_field": job_field,
            "dob": str(dob),
            "user_image": str(user_image) if user_image else None
        }
        email_password_data = {
            "email": email,
            "password": password
        }

        # Save user data to separate JSON files
        with open("user_data.json", "w") as user_file:
            json.dump(user_data, user_file, indent=4)
        with open("email_password_data.json", "w") as email_password_file:
            json.dump(email_password_data, email_password_file, indent=4)

        st.success("Form submitted successfully!")

# Display the uploaded image
if user_image is not None:
    st.image(user_image, caption="Uploaded Image", use_column_width=True)

# Additional features or functionalities can be added as needed


