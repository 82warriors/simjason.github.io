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

.explore-title{
    text-align:center;
    font-size:36px;
    font-weight:700;
    margin-top:40px;
    margin-bottom:30px;
}

.tile{
    padding:40px;
    border-radius:18px;
    background:#f8fafc;
    transition:all 0.25s ease;
    height:180px;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
}

.tile:hover{
    transform:translateY(-6px);
    box-shadow:0px 15px 35px rgba(0,0,0,0.15);
}

.tile-title{
    font-size:26px;
    font-weight:600;
}

.tile-desc{
    color:#6b7280;
    font-size:16px;
}

.tile-arrow{
    font-size:20px;
    font-weight:600;
    color:#6366f1;
    align-self:flex-end;
    transition:0.2s;
}

.tile:hover .tile-arrow{
    transform:translateX(6px);
}

.tile-link{
    text-decoration:none;
    color:inherit;
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


# ---------- METRICS ----------
st.markdown("<br>", unsafe_allow_html=True)

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


# ---------- EXPLORE ----------
st.markdown('<div class="explore-title">Explore</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.markdown("""
<a class="tile-link" href="?page=AboutMe">
<div class="tile">
<div>
<div class="tile-title">👤 About</div>
<div class="tile-desc">
Learn about my background, experience and technology journey.
</div>
</div>
<div class="tile-arrow">→</div>
</div>
</a>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<a class="tile-link" href="?page=Projects">
<div class="tile">
<div>
<div class="tile-title">⚙️ Projects</div>
<div class="tile-desc">
Explore automation systems, dashboards and digital platforms I built.
</div>
</div>
<div class="tile-arrow">→</div>
</div>
</a>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<a class="tile-link" href="?page=Experiences">
<div class="tile">
<div>
<div class="tile-title">💼 Experience</div>
<div class="tile-desc">
Professional experience leading ICT initiatives and digital transformation.
</div>
</div>
<div class="tile-arrow">→</div>
</div>
</a>
""", unsafe_allow_html=True)

with col4:
    st.markdown("""
<a class="tile-link" href="?page=Dashboard">
<div class="tile">
<div>
<div class="tile-title">📊 Dashboard</div>
<div class="tile-desc">
Interactive analytics dashboards and data visualisations.
</div>
</div>
<div class="tile-arrow">→</div>
</div>
</a>
""", unsafe_allow_html=True)


st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© Jason Sim")
