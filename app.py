import streamlit as st
import sqlite3
import json
from datetime import datetime

# Initialize connection to SQLite database
conn = sqlite3.connect('userdata.db', check_same_thread=False)
c = conn.cursor()

# Create tables for user data and credentials
def create_tables():
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            name TEXT,
            age INTEGER,
            sex TEXT,
            job_field TEXT,
            dob TEXT,
            email TEXT PRIMARY KEY,
            image BLOB
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_credentials (
            email TEXT PRIMARY KEY,
            password TEXT
        )
    ''')
    conn.commit()

# Function to insert user data
def insert_user_data(name, age, sex, job_field, dob, email, image):
    c.execute('''
        INSERT OR REPLACE INTO user_data (name, age, sex, job_field, dob, email, image)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, age, sex, job_field, dob, email, image))
    conn.commit()

# Function to insert user credentials
def insert_user_credentials(email, password):
    c.execute('''
        INSERT OR REPLACE INTO user_credentials (email, password)
        VALUES (?, ?)
    ''', (email, password))
    conn.commit()

# Function to check user credentials
def check_user_credentials(email, password):
    c.execute('''
        SELECT * FROM user_credentials WHERE email = ? AND password = ?
    ''', (email, password))
    return c.fetchone() is not None

# Function to retrieve all user data (for admin)
def get_all_user_data():
    c.execute('SELECT * FROM user_data')
    return c.fetchall()

st.title("Mams Nivash")

# Create tables
create_tables()

# Sidebar for navigation
page = st.sidebar.selectbox("Select Page", ["Registration", "Login", "Download User Details"])

if page == "Registration":
    st.header("User Registration")
    
    # User information inputs
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", value=None, min_value=18)
    sex = st.radio("Select Your Sex", ["Male", "Female"])
    job_field = st.selectbox("What is your Job field", ('Academic', 'IT', 'Real Estate Business', 'Local Business', 'Salesman', 'Manager', 'Medical'))
    dob = st.date_input("When's your birthday")
    email = st.text_input("Enter your E-Mail address")
    password = st.text_input("Create your password", type="password")
    confirm_password = st.text_input("Re-enter your password", type="password")
    user_image = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

    # Check if passwords match and register user
    if st.button("Register"):
        if not (password == confirm_password):
            st.error("Passwords do not match. Please re-enter matching passwords.")
        else:
            image_data = user_image.getvalue() if user_image else None
            insert_user_data(name, age, sex, job_field, dob, email, image_data)
            insert_user_credentials(email, password)
            st.success("Registration successful!")

elif page == "Login":
    st.header("User Login")
    
    # Login inputs
    login_email = st.text_input("Enter your E-Mail address")
    login_password = st.text_input("Enter your password", type="password")

    # Check if login credentials match
    if st.button("Login"):
        if check_user_credentials(login_email, login_password):
            st.success("Login successful!")
        else:
            st.error("Invalid login credentials. Please try again.")

elif page == "Download User Details":
    st.header("User Login As Admin")
    login_email = st.text_input("Enter your E-Mail address of admin")
    login_password = st.text_input("Enter your password of admin", type="password")

    if st.button("Login"):
        if login_email == "Rockarush2@gmail.com" and login_password == "Arush@2003":
            st.success("Login successful as Admin!")
            all_user_data = get_all_user_data()
            if st.button("Download user_data.json"):
                st.download_button(
                    label="Download user_data.json",
                    data=json.dumps(all_user_data, indent=4),
                    mime="application/json",
                    file_name="user_data.json",
                    key="user_data_download"
                )
        else:
            st.error("Invalid login credentials. Please try again.")

# Display the uploaded image on the registration page
if page == "Registration" and user_image is not None:
    st.image(user_image, caption="Uploaded Image", use_column_width=True)
