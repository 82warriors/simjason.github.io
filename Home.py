import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# ---------------- STYLE ----------------
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

.section-title{
    text-align:center;
    font-size:36px;
    font-weight:700;
    margin-top:50px;
    margin-bottom:30px;
}

.metric-box{
    text-align:center;
    padding:30px;
}

.metric-number{
    font-size:36px;
    font-weight:700;
}

.metric-label{
    color:#6b7280;
}

.project-card{
    padding:30px;
    border-radius:16px;
    background:#f8fafc;
    transition:0.25s;
}

.project-card:hover{
    transform:translateY(-6px);
    box-shadow:0px 15px 35px rgba(0,0,0,0.15);
}

.project-title{
    font-size:24px;
    font-weight:600;
}

.project-desc{
    color:#6b7280;
}

.nav-tile{
    padding:35px;
    border-radius:16px;
    background:#f8fafc;
    transition:0.25s;
}

.nav-tile:hover{
    transform:translateY(-6px);
    box-shadow:0px 15px 35px rgba(0,0,0,0.15);
}

.nav-title{
    font-size:22px;
    font-weight:600;
}

.nav-desc{
    color:#6b7280;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">

<div class="hero-title">
Jason Sim
</div>

<div class="hero-sub">
Website Analytics • Automation Systems • Data Dashboards
</div>

<div class="hero-desc">
Building digital systems that transform data into operational insights.
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- METRICS ----------------
st.markdown('<div class="section-title">Impact</div>', unsafe_allow_html=True)

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

# ---------------- FEATURED WORK ----------------
st.markdown('<div class="section-title">Featured Work</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="project-card">
<div class="project-title">⚙️ ICT Booking Automation</div>
<div class="project-desc">
Automated equipment booking workflow using Google Forms and Apps Script.
</div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="project-card">
<div class="project-title">📊 Inventory Dashboard</div>
<div class="project-desc">
Data dashboard analysing ICT asset usage and operational trends.
</div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="project-card">
<div class="project-title">🎓 MTD301 Media Project</div>
<div class="project-desc">
Digital media project exploring storytelling and platform engagement.
</div>
</div>
""", unsafe_allow_html=True)

# ---------------- EXPLORE ----------------
st.markdown('<div class="section-title">Explore</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
<div class="nav-tile">
<div class="nav-title">👤 About</div>
<div class="nav-desc">
Background and expertise
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/AboutMe.py", label="Open")

with col2:
    st.markdown("""
<div class="nav-tile">
<div class="nav-title">⚙️ Projects</div>
<div class="nav-desc">
Systems and platforms I built
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/Projects.py", label="Open")

with col3:
    st.markdown("""
<div class="nav-tile">
<div class="nav-title">💼 Experience</div>
<div class="nav-desc">
Professional journey
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/Experiences.py", label="Open")

with col4:
    st.markdown("""
<div class="nav-tile">
<div class="nav-title">📊 Dashboard</div>
<div class="nav-desc">
Interactive analytics
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/Dashboard.py", label="Open")

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© Jason Sim")
