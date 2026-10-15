import streamlit as st

def render_skills():
    st.subheader("🛠 Technical Skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 💻 Languages & Problem Solving")
        st.write("• **C++** (DSA, STL, Algorithms)")
        st.write("• **Python** (OOP, Metaprogramming, NumPy)")
        st.write("• **SQL** (PostgreSQL, Joins, Indexing)")

    with col2:
        st.markdown("#### 🤖 Machine Learning & Data")
        st.write("• **Core:** Scikit-Learn, Pandas, NumPy")
        st.write("• **Deep Learning:** PyTorch fundamentals")
        st.write("• **Techniques:** Feature Engineering, Drift, RAG")

    with col3:
        st.markdown("#### ⚙️ Engineering & Tools")
        st.write("• **Backend:** FastAPI, Streamlit, RESTful APIs")
        st.write("• **DevOps:** Docker, Git/GitHub Actions")
        st.write("• **Environment:** Linux, JupyterLab, VS Code")