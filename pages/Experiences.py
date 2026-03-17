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
    padding:20px;
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
<div class="role">Infocomm Technology Manager / Associate</div>
<div class="company">Ministry of Education (Schools)</div>
<div class="date">2018 – Present</div>

<div class="point">• Lead ICT and digital initiatives supporting teaching and learning technologies</div>
<div class="point">• Develop automation solutions using Google Apps Script to streamline workflows</div>
<div class="point">• Build analytics dashboards for operational reporting and decision making</div>
<div class="point">• Manage ICT infrastructure, assets and system implementation</div>
<div class="point">• Develop web-based systems and microsites for staff access and operations</div>
</div>
""", unsafe_allow_html=True)

# EXPERIENCE 2 (you can edit/add more)
st.markdown("""
<div class="exp-card">
<div class="role">Recruitment & Operations Support</div>
<div class="company">Previous Organisation</div>
<div class="date">Earlier Experience</div>

<div class="point">• Managed recruitment processes including sourcing and screening candidates</div>
<div class="point">• Published job advertisements across multiple platforms</div>
<div class="point">• Maintained company website and digital content</div>
<div class="point">• Provided staff training on systems and workflows</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.divider()

st.markdown("""
<div class="center">
<p>Continuously building technology solutions that create real impact 🚀</p>
</div>
""", unsafe_allow_html=True)
