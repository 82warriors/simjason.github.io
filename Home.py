import streamlit as st
from nav import navbar

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# Navbar
navbar()

# ---------- STYLE ----------
st.markdown("""
<style>

.hero-title{
font-size:56px;
font-weight:700;
background: linear-gradient(90deg,#6366F1,#4CC9F0);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.hero-sub{
font-size:22px;
color:#6B7280;
margin-top:10px;
}

.hero-text{
font-size:18px;
margin-top:20px;
color:#374151;
}

.section-title{
margin-top:60px;
color:#6366F1;
font-size:32px;
font-weight:600;
}

.card{
padding:25px;
border-radius:14px;
background:#F8FAFC;
transition:0.25s;
}

.card:hover{
transform:translateY(-6px);
box-shadow:0px 10px 30px rgba(0,0,0,0.1);
}

.profile-img img{
border-radius:18px;
}

</style>
""", unsafe_allow_html=True)


# ---------- HERO SECTION ----------

col1, col2 = st.columns([2,1])

with col1:

    st.markdown(
        '<div class="hero-title">Jason Sim</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-sub">Automation Systems • Website Analytics • Data Dashboards</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-text">'
        'I build automation systems, analytics dashboards and digital platforms '
        'that transform operational data into actionable insights.'
        '</div>',
        unsafe_allow_html=True
    )

with col2:

    st.markdown('<div class="profile-img">', unsafe_allow_html=True)
    st.image("images/jason.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


st.divider()


# ---------- WHAT I DO ----------

st.markdown('<div class="section-title">What I Do</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">
<h3>⚙️ Automation</h3>
<p>Workflow automation systems that improve efficiency and reduce manual processes.</p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<h3>📊 Analytics</h3>
<p>Data dashboards that provide operational insights and support decision making.</p>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">
<h3>💻 ICT Systems</h3>
<p>Digital platforms and ICT solutions supporting digital transformation.</p>
</div>
""", unsafe_allow_html=True)


st.divider()


# ---------- FEATURED PROJECTS ----------

st.markdown('<div class="section-title">Featured Projects</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">
<h3>ICT Booking Automation</h3>
<p>Automated booking and approval workflow for equipment management.</p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<h3>Inventory Dashboard</h3>
<p>Analytics dashboard tracking ICT assets and operational usage.</p>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">
<h3>Attendance Analytics</h3>
<p>Excel-based analytics system analysing attendance trends.</p>
</div>
""", unsafe_allow_html=True)
