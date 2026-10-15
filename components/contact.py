import streamlit as st
import urllib.parse

MY_EMAIL = "gangwarprashant56789@gmail.com"

def render_contact():
    st.subheader("📬 Get In Touch")

    col_form, _ = st.columns([3, 2])

    with col_form:
        name = st.text_input("Name", placeholder="Your Name")
        subject_input = st.text_input("Subject", placeholder="Project Inquiry / Job Opportunity")
        message = st.text_area("Message", placeholder="Write your message here...")

        if name and message:
            subject = f"Portfolio Contact: {subject_input if subject_input else 'Inquiry'} from {name}"
            body = f"Hi Prashant,\n\n{message}\n\nRegards,\n{name}"
            
            # URL encode params
            encoded_subject = urllib.parse.quote(subject)
            encoded_body = urllib.parse.quote(body)
            mailto_url = f"mailto:{MY_EMAIL}?subject={encoded_subject}&body={encoded_body}"

            st.markdown(f"""
                <a href="{mailto_url}" target="_blank" style="text-decoration: none;">
                    <div style="
                        background-color: #38BDF8;
                        color: #0F172A;
                        text-align: center;
                        padding: 12px;
                        border-radius: 8px;
                        font-weight: 700;
                        margin-top: 10px;
                        cursor: pointer;">
                        ✉️ Send via Gmail / Mail App
                    </div>
                </a>
            """, unsafe_allow_html=True)
        else:
            st.button("Send Message", disabled=True, use_container_width=True)
            st.caption("Name aur Message fill karein button activate karne ke liye.")