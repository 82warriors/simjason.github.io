import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>

.hero {
    text-align:center;
    padding:140px 20px;
    background: linear-gradient(120deg,#6366f1,#4cc9f0,#72efdd);
    border-radius:24px;
}

.hero-title {
    font-size:72px;
    font-weight:700;
    color:white;
}

.hero-sub {
    font-size:26px;
    color:white;
}

.hero-desc {
    font-size:18px;
    color:white;
    opacity:0.9;
}

.metric-box {
    text-align:center;
    padding:30px;
}

.metric-number {
    font-size:36px;
    font-weight:700;
}

.metric-label {
    color:#6b7280;
}

.section-title {
    text-align:center;
    font-size:36px;
    font-weight:700;
}

.nav-tile {
    text-align:center;
    padding:40px;
    border-radius:18px;
    background:#f8fafc;
    transition:0.25s;
}

.nav-tile:hover {
    transform:translateY(-6px);
    box-shadow:0px 12px 30px rgba(0,0,0,0.15);
}

.nav-title {
    font-size:26px;
    font-weight:600;
}

.nav-desc {
    color:#6b7280;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">

<div class="hero-title">
Jason Sim
</div>

<div class="hero-sub">
Website Analytics • Automation Systems • Data Dashboards
</div>

<div class="hero-desc">
Building data-driven digital systems that transform workflows and insights.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------- METRICS ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="metric-box">
<div class="metric-number">10+</div>
<div class="metric-label">Automation Systems</div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="metric-box">
<div class="metric-number">15+</div>
<div class="metric-label">Dashboards Built</div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="metric-box">
<div class="metric-number">20+</div>
<div class="metric-label">ICT Solutions</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- NAVIGATION ----------
st.markdown('<div class="section-title">Explore</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
<div class="nav-tile">
<div class="nav-title">👤 About</div>
<div class="nav-desc">
Who I am and what I do
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/AboutMe.py", label="Explore")

with col2:
    st.markdown("""
<div class="nav-tile">
<div class="nav-title">⚙️ Projects</div>
<div class="nav-desc">
Systems and platforms I built
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/Projects.py", label="Explore")

with col3:
    st.markdown("""
<div class="nav-tile">
<div class="nav-title">💼 Experience</div>
<div class="nav-desc">
Professional journey
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/Experiences.py", label="Explore")

with col4:
    st.markdown("""
<div class="nav-tile">
<div class="nav-title">📊 Dashboard</div>
<div class="nav-desc">
Interactive analytics work
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/Dashboard.py", label="Explore")

st.markdown("<br><br>", unsafe_allow_html=True)

st.caption("© Jason Sim")
