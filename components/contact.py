import streamlit as st

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
                if sender_name and sender_email and message:
                    st.success("Thank you! Your message has been sent successfully.")
                else:
                    st.error("Please fill in all fields.")