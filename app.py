import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Prashant Gangwar | AI & DS Engineer Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
    /* Global Base */
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Availability Badge */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        color: #10B981;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 16px;
    }
    .status-dot {
        width: 8px;
        height: 8px;
        background-color: #10B981;
        border-radius: 50%;
        box-shadow: 0 0 10px #10B981;
    }

    /* Hero Gradient Text */
    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        line-height: 1.15;
        background: linear-gradient(135deg, #FFFFFF 30%, #38BDF8 70%, #818CF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 12px;
    }

    .hero-subtitle {
        color: #94A3B8;
        font-size: 1.15rem;
        line-height: 1.6;
        margin-bottom: 24px;
    }

    /* Terminal Window Mockup */
    .terminal-container {
        background: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 12px;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
        overflow: hidden;
        margin-top: 10px;
    }
    .terminal-header {
        background: #1E293B;
        padding: 10px 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .terminal-btn {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }
    .btn-red { background: #EF4444; }
    .btn-yellow { background: #F59E0B; }
    .btn-green { background: #10B981; }
    .terminal-title {
        color: #64748B;
        font-size: 0.75rem;
        font-family: 'Fira Code', monospace;
        margin-left: 8px;
    }
    .terminal-body {
        padding: 18px 20px;
        font-family: 'Fira Code', monospace;
        font-size: 0.88rem;
        color: #E2E8F0;
        line-height: 1.6;
    }
    .t-keyword { color: #F43F5E; }
    .t-func { color: #38BDF8; }
    .t-str { color: #A3E635; }
    .t-comment { color: #64748B; font-style: italic; }

    /* Modern Metric Cards */
    .stat-card {
        background: linear-gradient(145deg, #1E293B, #0F172A);
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 20px 18px;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stat-card:hover {
        border-color: #38BDF8;
        transform: translateY(-5px);
        box-shadow: 0 10px 25px -5px rgba(56, 189, 248, 0.2);
    }
    .stat-num {
        font-size: 2.2rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 4px;
    }
    .stat-desc {
        color: #94A3B8;
        font-size: 0.82rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.75px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR -----------------
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
    st.download_button(
        label="📄 Download Resume (PDF)",
        data=b"Sample resume content. Replace with actual file bytes.",
        file_name="Prashant_Gangwar_Resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )

# ----------------- HERO SECTION -----------------

# 1. Availability Status Pill
st.markdown("""
<div class="status-badge">
    <div class="status-dot"></div>
    Available for Summer 2027 / 2028 Internships
</div>
""", unsafe_allow_html=True)

# 2. Main Hero Grid
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
    
    # Action buttons
    btn_col1, btn_col2, _ = st.columns([1.2, 1.2, 1])
    with btn_col1:
        st.link_button("🚀 View Projects", "#featured-projects", use_container_width=True)
    with btn_col2:
        st.link_button("💼 Connect on LinkedIn", "https://linkedin.com", use_container_width=True)

with hero_right:
    # Interactive/Visual Terminal Window Mockup
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

# 3. Interactive KPI Highlight Cards
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-num">160+</div>
        <div class="stat-desc">DSA Problems Solved</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-num">9.8</div>
        <div class="stat-desc">Year 1 CGPA</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-num">&lt; 50ms</div>
        <div class="stat-desc">Target API Latency</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-num">100%</div>
        <div class="stat-desc">Dockerized Projects</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ----------------- SKILLS MATRIX -----------------
st.subheader("🛠 Technical Skills")

skill_col1, skill_col2, skill_col3 = st.columns(3)

with skill_col1:
    st.markdown("#### 💻 Languages & Problem Solving")
    st.write("• **C++** (DSA, STL, Algorithms)")
    st.write("• **Python** (OOP, Metaprogramming, NumPy)")
    st.write("• **SQL** (PostgreSQL, Joins, Indexing)")

with skill_col2:
    st.markdown("#### 🤖 Machine Learning & Data")
    st.write("• **Core:** Scikit-Learn, Pandas, NumPy")
    st.write("• **Deep Learning:** PyTorch fundamentals")
    st.write("• **Techniques:** Feature Engineering, Drift, RAG")

with skill_col3:
    st.markdown("#### ⚙️ Engineering & Tools")
    st.write("• **Backend:** FastAPI, Streamlit, RESTful APIs")
    st.write("• **DevOps:** Docker, Git/GitHub Actions")
    st.write("• **Environment:** Linux, JupyterLab, VS Code")

st.markdown("---")

# ----------------- FEATURED PROJECTS -----------------
st.subheader("🚀 Featured Projects")

projects = [
    {
        "title": "End-to-End Predictive Diagnostic Pipeline & Microservice",
        "description": "Production-ready predictive service exposing trained Scikit-Learn classification models via asynchronous FastAPI endpoints. Features Pydantic input validation, low-latency scoring, Dockerized container deployment, and a Streamlit client.",
        "tags": ["Python", "FastAPI", "Scikit-Learn", "Docker", "Streamlit"],
        "github": "https://github.com/",
        "demo": "https://streamlit.io/"
    },
    {
        "title": "Domain-Specific Semantic Search & RAG System",
        "description": "Information retrieval pipeline utilizing vector embeddings, FAISS indexing, and hybrid lexical-semantic ranking. Enables zero-shot natural language querying over technical documentation with source citation.",
        "tags": ["Python", "FAISS", "Embeddings", "FastAPI", "VectorDB"],
        "github": "https://github.com/",
        "demo": "https://github.com/"
    },
    {
        "title": "Algorithmic Problem Solutions & Pattern Library",
        "description": "Clean, optimized C++ and Python implementations of 160+ algorithmic challenges categorized by pattern (Sliding Window, Two Pointers, Monotonic Stack, Backtracking, and Binary Search).",
        "tags": ["C++", "Python", "Data Structures", "Algorithms"],
        "github": "https://github.com/",
        "demo": "https://leetcode.com/"
    }
]

for proj in projects:
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

st.markdown("---")

# ----------------- CONTACT FORM -----------------
st.subheader("📬 Get In Touch")

col_form, col_text = st.columns([3, 2])

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
                st.error("Please fill in all fields")

