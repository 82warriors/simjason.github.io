import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="centered"
)

st.title("Jason Sim")
st.write("Technology Advocate")
st.write("Automation Systems | Website Analytics | Data Dashboards")

st.markdown("---")

# CARD STYLE
st.markdown("""
<style>
.card {
    padding:20px;
    border-radius:10px;
    border:1px solid #e6e6e6;
    text-align:center;
    margin-bottom:15px;
    background-color:#f9f9f9;
}
.card:hover {
    box-shadow:0px 4px 12px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# CARDS
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <h3>About</h3>
        <p>Who I am and what I do.</p>
    </div>
    """, unsafe_allow_html=True)

    st.page_link("pages/AboutMe.py", label="Open")

with col2:
    st.markdown("""
    <div class="card">
        <h3>Projects</h3>
        <p>Systems and platforms I built.</p>
    </div>
    """, unsafe_allow_html=True)

    st.page_link("pages/projects.py", label="Open")

with col3:
    st.markdown("""
    <div class="card">
        <h3>Portfolio</h3>
        <p>Digital platforms and analytics work.</p>
    </div>
    """, unsafe_allow_html=True)

    st.page_link("pages/portfolio.py", label="Open")

with col4:
    st.markdown("""
    <div class="card">
        <h3>Dashboard</h3>
        <p>Interactive analytics dashboard.</p>
    </div>
    """, unsafe_allow_html=True)

    st.page_link("pages/dashboard.py", label="Open")

st.markdown("---")
st.caption("© Jason Sim")
