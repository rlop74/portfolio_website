import streamlit as st

st.set_page_config(layout="wide")

st.header("Let's connect!")

with st.form(key="contact_form"):
    user_email = st.text_input(label="Your email address")
    user_message = st.text_area("Your message")
    submitted = st.form_submit_button("Submit")

    if submitted:
        print(user_email)
        print(user_message)
        print("Dudong nambawan")