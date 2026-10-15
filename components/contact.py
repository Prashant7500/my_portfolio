import streamlit as st
import urllib.parse

RECEIVER_EMAIL = "gangwarprashant7983@gmail.com"

def render_contact():
    st.subheader("📬 Get In Touch")

    col_form, _ = st.columns([3, 2])

    with col_form:
        name = st.text_input("Name", placeholder="Your Name")
        subject_input = st.text_input("Subject", placeholder="Project Inquiry / Job Opportunity")
        message = st.text_area("Message", placeholder="Let's connect regarding opportunities...")

        if name.strip() and message.strip():
            subject = f"Portfolio Inquiry from {name.strip()}"
            if subject_input.strip():
                subject = f"{subject_input.strip()} - {name.strip()}"

            body = f"Hi Prashant,\n\n{message.strip()}\n\nRegards,\n{name.strip()}"

            # Direct Gmail Web URL
            params = {
                "view": "cm",
                "fs": "1",
                "to": RECEIVER_EMAIL,
                "su": subject,
                "body": body
            }
            gmail_url = f"https://mail.google.com/mail/?{urllib.parse.urlencode(params)}"

            st.link_button("🚀 Open in Gmail to Send", gmail_url, type="primary", use_container_width=True)
            st.caption("ℹ️ Email aapke authenticated Gmail account se directly deliver hogi.")
        else:
            st.button("Open in Gmail to Send", disabled=True, use_container_width=True)
            st.caption("Name aur Message fill karein button activate karne ke liye.")