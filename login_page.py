import streamlit as st

USERNAME = "admin"
PASSWORD = "password123"

st.title('Login')

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    with st.form(key='login_form'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submit_button = st.form_submit_button('Login')

if submit_button:
    
    if username == USERNAME and password == PASSWORD:
        st.success("Login successful!")
        st.write("Welcome to the application!")
        
    else:
        st.error("Invalid username or password. Please try again.")
