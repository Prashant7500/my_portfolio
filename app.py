import streamlit as st
import sys
from pathlib import Path

# Path fix taaki components sahi se load hon
sys.path.append(str(Path(__file__).parent))

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

# 2. Inject CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# 3. Render Sidebar
render_sidebar()

# 4. Render Main Sections
render_hero()
st.markdown("---")

render_skills()
st.markdown("---")

render_projects()
st.markdown("---")

render_contact()