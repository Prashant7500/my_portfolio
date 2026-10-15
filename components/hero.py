import streamlit as st

def render_hero():
    st.markdown("""
    <div class="status-badge">
        <div class="status-dot"></div>
        Available for Summer 2027 / 2028 Internships
    </div>
    """, unsafe_allow_html=True)

    hero_left, hero_right = st.columns([1.3, 1], gap="large")

    with hero_left:
        st.markdown("""
        <div class="hero-title">
            Engineering Intelligent Systems & Scalable ML Pipelines.
        </div>
        <div class="hero-subtitle">
            Hi, I'm <b>Prashant Gangwar</b> — an AI & Data Science engineer focused on low-latency inference, production-grade microservices, and core algorithms.
        </div>
        """, unsafe_allow_html=True)
        
        btn_col1, btn_col2, _ = st.columns([1.2, 1.2, 1])
        with btn_col1:
            st.link_button("🚀 View Projects", "#featured-projects", use_container_width=True)
        with btn_col2:
            st.link_button("💼 Connect on LinkedIn", "https://linkedin.com", use_container_width=True)

    with hero_right:
        st.markdown("""
        <div class="terminal-container">
            <div class="terminal-header">
                <span class="terminal-btn btn-red"></span>
                <span class="terminal-btn btn-yellow"></span>
                <span class="terminal-btn btn-green"></span>
                <span class="terminal-title">engineer_profile.py</span>
            </div>
            <div class="terminal-body">
                <span class="t-keyword">class</span> <span class="t-func">Candidate</span>:<br>
                &nbsp;&nbsp;name = <span class="t-str">"Prashant Gangwar"</span><br>
                &nbsp;&nbsp;role = <span class="t-str">"AI & Data Science Undergrad"</span><br>
                &nbsp;&nbsp;stack = [<span class="t-str">"Python"</span>, <span class="t-str">"C++"</span>, <span class="t-str">"FastAPI"</span>, <span class="t-str">"PyTorch"</span>]<br>
                &nbsp;&nbsp;focus = [<span class="t-str">"MLOps"</span>, <span class="t-str">"DSA"</span>, <span class="t-str">"Microservices"</span>]<br><br>
                <span class="t-comment"># Current Execution</span><br>
                <span class="t-keyword">def</span> <span class="t-func">status</span>():<br>
                &nbsp;&nbsp;<span class="t-keyword">return</span> <span class="t-str">"Shipping robust inference APIs & solving algorithms"</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    c1, c2, c3, c4 = st.columns(4)
    stats = [
        ("160+", "DSA Problems Solved"),
        ("9.8", "Year 1 CGPA"),
        ("< 50ms", "Target API Latency"),
        ("100%", "Dockerized Projects")
    ]
    for col, (num, desc) in zip([c1, c2, c3, c4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-num">{num}</div>
                <div class="stat-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)