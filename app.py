import streamlit as st
from styles import CUSTOM_CSS
from components.sidebar import render_sidebar
from components.hero import render_hero
from components.skills import render_skills
from components.projects import render_projects
from components.contact import render_contact

# 1. Page Configuration
st.set_page_config(
    page_title="Prashant Gangwar | AI & DS Engineer Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Global Styles
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Purana tarika (5 lines) hatakar simple ye likh sakte hain:
from components import (
    render_sidebar,
    render_hero,
    render_skills,
    render_projects,
    render_contact
)