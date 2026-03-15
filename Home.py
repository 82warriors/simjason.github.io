import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# ---------------- STYLE ----------------
st.markdown("""
<style>

.hero-container{
    padding-top:120px;
    padding-bottom:80px;
    text-align:center;
}

.hero-title{
    font-size:64px;
    font-weight:700;
}

.hero-highlight{
    background: linear-gradient(90deg,#6366f1,#4cc9f0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub{
    font-size:24px;
    color:#6b7280;
    margin-top:10px;
}

.hero-desc{
    font-size:18px;
    color:#6b7280;
    max-width:700px;
    margin:auto;
    margin-top:20px;
}

.section-title{
    text-align:center;
    font-size:32px;
    font-weight:700;
    margin-top:50px;
    margin-bottom:30px;
}

.metric{
    text-align:center;
}

.metric-number{
    font-size:36px;
    font-weight:700;
}

.metric-label{
    color:#6b7280;
}

.card{
    padding:30px;
    border-radius:16px;
    background:#f8fafc;
    transition:0.25s;
}

.card:hover{
    transform:translateY(-6px);
    box-shadow:0px 15px 35px rgba(0,0,0,0.15);
}

.card-title{
    font-size:22px;
    font-weight:600;
}

.card-desc{
    color:#6b7280;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HERO ----------------

st.markdown("""
<div class="hero-container">

<div class="hero-title">
Jason <span class="hero-highlight">Sim</span>
</div>

<div class="hero-sub">
Automation Systems • Website Analytics • Data Dashboards
</div>

<div class="hero-desc">
I design automation systems, analytics dashboards and digital platforms
that simplify workflows and transform operational data into insights.
</div>

</div>
""", unsafe_allow_html=True)


# ---------------- IMPACT ----------------

st.markdown('<div class="section-title">Impact</div>', unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="metric">
<div class="metric-number">10+</div>
<div class="metric-label">Automation Systems</div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="metric">
<div class="metric-number">15+</div>
<div class="metric-label">Dashboards Built</div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="metric">
<div class="metric-number">20+</div>
<div class="metric-label">ICT Solutions</div>
</div>
""", unsafe_allow_html=True)


# ---------------- FEATURED WORK ----------------

st.markdown('<div class="section-title">Featured Work</div>', unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">
<div class="card-title">⚙️ ICT Booking Automation</div>
<div class="card-desc">
Automated equipment booking workflow using Google Forms and Apps Script.
</div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<div class="card-title">📊 Inventory Dashboard</div>
<div class="card-desc">
Data dashboard analysing ICT asset usage and operational trends.
</div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">
<div class="card-title">🎓 MTD301 Media Project</div>
<div class="card-desc">
Digital media storytelling project exploring platform engagement.
</div>
</div>
""", unsafe_allow_html=True)


# ---------------- EXPLORE ----------------

st.markdown('<div class="section-title">Explore</div>', unsafe_allow_html=True)

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown("""
<div class="card">
<div class="card-title">👤 AboutMe</div>
<div class="card-desc">
Background, expertise and interests.
</div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<div class="card-title">⚙️ Projects</div>
<div class="card-desc">
Automation systems and digital platforms.
</div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">
<div class="card-title">💼 Experiences</div>
<div class="card-desc">
Professional journey and achievements.
</div>
</div>
""", unsafe_allow_html=True)

with col4:
    st.markdown("""
<div class="card">
<div class="card-title">📊 Dashboard</div>
<div class="card-desc">
Interactive analytics and visualisations.
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>")
st.caption("© Jason Sim")
