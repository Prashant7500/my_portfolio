import streamlit as st
from pathlib import Path

RESUME_PATH = Path("assets/Prashant_Gangwar_Resume.pdf")

def render_sidebar():
    with st.sidebar:
        st.markdown("## ⚡ Prashant Gangwar")
        st.caption("AI & Data Science Undergrad | SLIET")
        
        st.markdown("---")
        st.markdown("### 📍 Quick Info")
        st.write("🎯 **Focus:** Machine Learning, Systems & DSA")
        st.write("💻 **Primary Stack:** Python, C++, FastAPI, PyTorch")
        st.write("🎓 **Expected Graduation:** 2029")
        
        st.markdown("---")
        st.markdown("### 🔗 Connect")
        st.markdown("""
        - [GitHub](https://github.com/)
        - [LinkedIn](https://linkedin.com/)
        - [LeetCode](https://leetcode.com/)
        """)
        
        st.markdown("---")
        
        if RESUME_PATH.is_file():
            with open(RESUME_PATH, "rb") as pdf_file:
                resume_bytes = pdf_file.read()
        else:
            resume_bytes = b"%PDF-1.4 Mock resume file placeholder"

        st.download_button(
            label="📄 Download Resume (PDF)",
            data=resume_bytes,
            file_name="Prashant_Gangwar_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )