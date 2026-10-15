import sys
from pathlib import Path
import streamlit as st

# 1. Project root ko Python system path me insert karna taaki modules safely import hon
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# 2. Page Configuration (Ye command hamesha pehle execute honi chahiye)
st.set_page_config(
    page_title="Prashant Gangwar | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 3. Custom CSS Loading (Fallback ke sath)
try:
    from styles import CUSTOM_CSS
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
except Exception as e:
    st.warning(f"Styles load hone me issue: {e}")

# 4. Components Safe Execution
def main():
    # Sidebar
    try:
        from components.sidebar import render_sidebar
        render_sidebar()
    except Exception as e:
        st.sidebar.error(f"Sidebar error: {e}")

    # Hero Section
    try:
        from components.hero import render_hero
        render_hero()
    except Exception as e:
        st.error(f"Hero section error: {e}")

    st.markdown("---")

    # Skills Section
    try:
        from components.skills import render_skills
        render_skills()
    except Exception as e:
        st.error(f"Skills section error: {e}")

    st.markdown("---")

    # Projects Section
    try:
        from components.projects import render_projects
        render_projects()
    except Exception as e:
        st.error(f"Projects section error: {e}")

    st.markdown("---")

    # Contact Section
    try:
        from components.contact import render_contact
        render_contact()
    except Exception as e:
        st.error(f"Contact section error: {e}")

if __name__ == "__main__":
    main()