import streamlit as st

st.set_page_config(page_title="Jason Sim", page_icon="🚀", layout="wide")

# HERO
st.markdown("""
<h1 style='text-align:center;font-size:60px;'>Jason Sim</h1>
<p style='text-align:center;font-size:22px;color:gray;'>
Technology Advocate • Website Analytics • Automation Systems
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# CARD STYLE
st.markdown("""
<style>

.card {
    padding:35px;
    border-radius:14px;
    border:1px solid #e6e6e6;
    background: linear-gradient(135deg,#f8f9fa,#ffffff);
    text-align:center;
    transition:0.2s;
}

.card:hover {
    transform:translateY(-6px);
    box-shadow:0px 10px 25px rgba(0,0,0,0.15);
}

.card-title {
    font-size:24px;
    font-weight:600;
}

.card-desc {
    font-size:14px;
    color:#666;
}

</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# ABOUT CARD
with col1:
    st.markdown("""
<div class="card">
<div style="font-size:36px">👤</div>
<div class="card-title">About</div>
<div class="card-desc">
Learn more about my background and expertise.
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Open", key="about"):
        st.switch_page("pages/AboutMe.py")


# PROJECTS CARD
with col2:
    st.markdown("""
<div class="card">
<div style="font-size:36px">⚙️</div>
<div class="card-title">Projects</div>
<div class="card-desc">
Systems, automation tools and digital platforms I built.
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Open", key="projects"):
        st.switch_page("pages/projects.py")


# PORTFOLIO CARD
with col3:
    st.markdown("""
<div class="card">
<div style="font-size:36px">📊</div>
<div class="card-title">Portfolio</div>
<div class="card-desc">
Technology initiatives, analytics work and digital platforms.
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Open", key="portfolio"):
        st.switch_page("pages/portfolio.py")


# DASHBOARD CARD
with col4:
    st.markdown("""
<div class="card">
<div style="font-size:36px">📈</div>
<div class="card-title">Dashboard</div>
<div class="card-desc">
Interactive analytics dashboards and visualisations.
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Open", key="dashboard"):
        st.switch_page("pages/dashboard.py")

st.markdown("---")
st.caption("© Jason Sim")
