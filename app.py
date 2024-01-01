import streamlit as st
import json

st.title("Mams Nivash")

# Sidebar for navigation
page = st.sidebar.selectbox("Select Page", ["Registration", "Login","Download User Datails"])

if page == "Registration":
    st.header("User Registration")
    
    # User information inputs
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", value=None, min_value=18)
    sex = st.radio("Select Your Sex", ["Male", "Female"])
    job_field = st.selectbox("What is your Job field", ('Academic', 'IT', 'Real Estate Business', 'Local Business', 'Salesman', 'Manager', 'Medical'))
    dob = st.date_input("When's your birthday")

    # Upload user image
    user_image = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

    # Email and Password
    email = st.text_input("Enter your E-Mail address")
    password = st.text_input("Create your password", type="password")
    confirm_password = st.text_input("Re-enter your password", type="password")

    # Check if passwords match
    passwords_match = password == confirm_password

    # Submit button for registration
    if st.button("Register"):
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

            st.success("Registration successful!")

elif page == "Login":
    st.header("User Login")
    
    # Login inputs
    login_email = st.text_input("Enter your E-Mail address")
    login_password = st.text_input("Enter your password", type="password")

    # Load email and password data from JSON file
    with open("email_password_data.json", "r") as email_password_file:
        email_password_data = json.load(email_password_file)

    # Check if login credentials match
    if st.button("Login"):
        if login_email == email_password_data["email"] and login_password == email_password_data["password"]:
            st.success("Login successful!")
        else:
            st.error("Invalid login credentials. Please try again.")
elif page == "Download User Datails":
    st.header("User Login As Admin")
    login_email = st.text_input("Enter your E-Mail address of admin")
    login_password = st.text_input("Enter your password of admin", type="password")

    # Load email and password data from JSON file
    with open("email_password_data.json", "r") as email_password_file:
        email_password_data = json.load(email_password_file)

    # Check if login credentials match
    if st.button("Login"):
        if login_email == "Rockarush2@gmail.com" and login_password == "Arush@2003":
            st.success("Login successful as Admin!")
            if st.button("Download user_data.json"):
                with open("user_data.json", "r") as user_file:
                    user_data = json.load(user_file)
                st.download_button(
                    label="Download user_data.json",
                    data=json.dumps(user_data, indent=4),
                    key="user_data_download"
                )
        else:
            st.error("Invalid login credentials. Please try again.")

# Display the uploaded image on the registration page
if page == "Registration" and user_image is not None:
    st.image(user_image, caption="Uploaded Image", use_column_width=True)

