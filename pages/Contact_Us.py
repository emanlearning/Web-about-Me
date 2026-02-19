import streamlit as st
from send_email import send_emails

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email:")
    raw_message = st.text_area("Your message:")
    submit = st.form_submit_button("Submit")
    message = f"""\
Subject: Email from {user_email}

from:{user_email}
{raw_message}
"""
    if submit:
        send_emails(message)
        st.info("Email sent successfully!")
