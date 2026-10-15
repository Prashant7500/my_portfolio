import streamlit as st
from data.projects_data import PORTFOLIO_PROJECTS

def render_projects():
    st.markdown('<div id="featured-projects"></div>', unsafe_allow_html=True)
    st.subheader("🚀 Featured Projects")

    for proj in PORTFOLIO_PROJECTS:
        tags_html = "".join([f'<span class="tech-pill">{t}</span>' for t in proj["tags"]])
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{proj['title']}</div>
            <div class="project-desc">{proj['description']}</div>
            <div>{tags_html}</div>
        </div>
        """, unsafe_allow_html=True)
        
        col_demo, col_gh, _ = st.columns([1, 1, 4])
        with col_demo:
            st.link_button("🌐 Live App", proj["demo"], use_container_width=True)
        with col_gh:
            st.link_button("💻 GitHub Repo", proj["github"], use_container_width=True)
        st.write("")