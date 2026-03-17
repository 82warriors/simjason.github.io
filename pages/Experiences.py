import streamlit as st
from nav import navbar

st.set_page_config(
    page_title="Experience | Jason Sim",
    page_icon="💼",
    layout="wide"
)

# Navbar
navbar()

# ---------- STYLE ----------
st.markdown("""
<style>

.section-title{
    margin-top:20px;
    color:#6366F1;
    font-size:36px;
    font-weight:700;
}

.timeline{
    border-left:3px solid #6366F1;
    margin-left:20px;
    padding-left:20px;
}

.exp-card{
    background:#ffffff;
    border-radius:14px;
    padding:22px;
    margin-bottom:25px;
    border:1px solid #e5e7eb;
    transition:0.3s;
}

.exp-card:hover{
    transform:translateY(-4px);
    box-shadow:0px 10px 25px rgba(0,0,0,0.08);
}

.role{
    font-size:20px;
    font-weight:600;
    color:#111827;
}

.company{
    font-size:16px;
    color:#6366F1;
    margin-bottom:6px;
}

.date{
    font-size:14px;
    color:#6B7280;
    margin-bottom:10px;
}

.point{
    margin-left:10px;
    font-size:15px;
    color:#374151;
    margin-bottom:6px;
}

.icon{
    font-size:22px;
    margin-right:8px;
}

.center{
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="section-title">💼 Experience</div>', unsafe_allow_html=True)

st.markdown("""
A summary of my experience in ICT management, automation systems and digital transformation.
""")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- TIMELINE ----------
st.markdown('<div class="timeline">', unsafe_allow_html=True)

# EXPERIENCE 1
st.markdown("""
<div class="exp-card">

<div class="role">
<span class="icon">🚀</span>
Infocomm Technology Manager / Associate
</div>

<div class="company">Ministry of Education (Schools)</div>
<div class="date">2018 – Present</div>

<div class="point">✅ Spearheaded ICT and digital initiatives supporting teaching and learning environments</div>
<div class="point">⚙️ Automated workflows using Google Apps Script, reducing manual processes significantly</div>
<div class="point">📊 Developed analytics dashboards to support data-driven decision making</div>
<div class="point">🖥️ Managed ICT infrastructure, assets and deployment across school operations</div>
<div class="point">🌐 Built web-based systems and microsites to centralise ICT services and improve accessibility</div>

</div>
""", unsafe_allow_html=True)

# EXPERIENCE 2
st.markdown("""
<div class="exp-card">

<div class="role">
<span class="icon">📌</span>
Recruitment & Operations Support
</div>

<div class="company">Previous Organisation</div>
<div class="date">Earlier Experience</div>

<div class="point">👥 Managed end-to-end recruitment processes including sourcing, screening and onboarding</div>
<div class="point">📢 Published job advertisements across multiple platforms to attract talent</div>
<div class="point">🌐 Maintained and updated company website to support digital outreach</div>
<div class="point">🎓 Trained staff on systems, workflows and operational tools</div>

</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.divider()

st.markdown("""
<div class="center">
<p>Driven by building systems that create efficiency and impact 🚀</p>
</div>
""", unsafe_allow_html=True)
