import streamlit as st

st.set_page_config(page_title="Jason Sim", page_icon="🚀", layout="wide")

# HERO SECTION
st.markdown("""
<style>

.hero {
    text-align:center;
    padding:80px 20px;
}

.hero-title {
    font-size:60px;
    font-weight:700;
}

.hero-sub {
    font-size:22px;
    color:#666;
}

.grid-card {
    padding:30px;
    border-radius:14px;
    border:1px solid #e6e6e6;
    background: linear-gradient(135deg,#f8f9fa,#ffffff);
    text-align:center;
    transition:0.2s;
}

.grid-card:hover {
    transform:translateY(-6px);
    box-shadow:0px 10px 25px rgba(0,0,0,0.15);
}

.card-icon {
    font-size:36px;
}

.card-title {
    font-size:22px;
    font-weight:600;
}

.card-desc {
    font-size:14px;
    color:#666;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<div class="hero-title">Jason Sim</div>
<div class="hero-sub">
Technology Advocate • Website Analytics • Automation Systems
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# GRID CARD LAYOUT
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# ABOUT
with col1:
    st.markdown("""
<div class="grid-card">
<div class="card-icon">👤</div>
<div class="card-title">About</div>
<div class="card-desc">
Learn more about my background, experience
and technology expertise.
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Open About"):
        st.switch_page("pages/AboutMe.py")


# PROJECTS
with col2:
    st.markdown("""
<div class="grid-card">
<div class="card-icon">⚙️</div>
<div class="card-title">Projects</div>
<div class="card-desc">
Explore automation systems, platforms
and dashboards I have built.
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Open Projects"):
        st.switch_page("pages/projects.py")


# PORTFOLIO
with col3:
    st.markdown("""
<div class="grid-card">
<div class="card-icon">📊</div>
<div class="card-title">Portfolio</div>
<div class="card-desc">
Digital platforms, analytics initiatives
and technology projects.
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Open Portfolio"):
        st.switch_page("pages/portfolio.py")


# DASHBOARD
with col4:
    st.markdown("""
<div class="grid-card">
<div class="card-icon">📈</div>
<div class="card-title">Dashboard</div>
<div class="card-desc">
Interactive analytics dashboards and
data visualisations.
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Open Dashboard"):
        st.switch_page("pages/dashboard.py")

st.markdown("---")

st.caption("© Jason Sim")
