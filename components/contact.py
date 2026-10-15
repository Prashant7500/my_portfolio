import streamlit as st
import urllib.parse

# Yahan apni actual Gmail ID dalein
RECEIVER_EMAIL = "gangwarprashant7983@gmail.com"

def render_contact():
    st.subheader("📬 Get In Touch")

    col_form, _ = st.columns([3, 2])

    with col_form:
        name = st.text_input("Name", placeholder="Your Name")
        subject_input = st.text_input("Subject", placeholder="Project Inquiry / Job Opportunity")
        message = st.text_area("Message", placeholder="Write your message here...")

        if name.strip() and message.strip():
            subject = f"Portfolio Inquiry from {name.strip()}"
            if subject_input.strip():
                subject = f"{subject_input.strip()} - from {name.strip()}"

            body = f"Hi Prashant,\n\n{message.strip()}\n\nRegards,\n{name.strip()}"

            # Direct Web Gmail Compose URL (100% browser me khulega)
            params = {
                "view": "cm",
                "fs": "1",
                "to": RECEIVER_EMAIL,
                "su": subject,
                "body": body
            }
            gmail_url = f"https://mail.google.com/mail/?{urllib.parse.urlencode(params)}"

            # Streamlit ka built-in link_button
            st.link_button(
                "🚀 Send via Gmail",
                gmail_url,
                type="primary",
                use_container_width=True
            )
        else:
            st.button("Send via Gmail", disabled=True, use_container_width=True)
            st.caption("Name aur Message enter karein button activate karne ke liye.")         
            st.caption("Name aur Message fill karein button activate karne ke liye.")