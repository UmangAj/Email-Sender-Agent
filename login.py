import streamlit as st
from config import EMAIL_ID, PASSWORD

# Set up initial variables (Email and password are defined in config)
actual_email = EMAIL_ID
actual_password = PASSWORD

def login_page():
    """Displays a login form and validates user credentials."""
    with st.form(key="login_form"):
        st.markdown("#### Enter your credentials")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            if email == actual_email and password == actual_password:
                return True
            else:
                # st.error("Invalid credentials. Please try again.")
                return False
    return None

# # Main code for controlling the flow
# login = login_page()

# if login is None:
#     st.write("Please log in.")
# elif login:
#     st.write("Hello! You have successfully logged in.")
# else:
#     st.write("Login failed, please try again.")
