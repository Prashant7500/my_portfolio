import streamlit as st
import requests

# Yahan apni actual email ID dalein jahan message receive karna hai
RECEIVER_EMAIL = "gangwarprashant7983@gmail.com"

def render_contact():
    st.subheader("📬 Get In Touch")

    col_form, _ = st.columns([3, 2])

    with col_form:
        with st.form("contact_form", clear_on_submit=True):
            sender_name = st.text_input("Name", placeholder="Your Name")
            sender_email = st.text_input("Email", placeholder="you@example.com")
            message = st.text_area("Message", placeholder="Let's connect regarding opportunities...")
            submitted = st.form_submit_button("Send Message", use_container_width=True)
            
            if submitted:
                if not sender_name or not sender_email or not message:
                    st.error("Please fill in all fields.")
                else:
                    # FormSubmit API endpoint
                    webhook_url = f"https://formsubmit.co/{RECEIVER_EMAIL}"
                    payload = {
                        "name": sender_name,
                        "email": sender_email,
                        "message": message,
                        "_subject": f"New Portfolio Message from {sender_name}",
                        "_captcha": "false"  # Automated spam captcha bypass
                    }
                    
                    try:
                        response = requests.post(webhook_url, data=payload)
                        if response.status_code == 200:
                            st.success("Thank you! Your message has been sent directly to my inbox.")
                        else:
                            st.error("Something went wrong. Please try reaching out via LinkedIn or email directly.")
                    except Exception as e:
                        st.error(f"Error sending message: {e}")