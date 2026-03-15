import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# -------- HIDE SIDEBAR --------
st.markdown("""
<style>

[data-testid="stSidebar"] {
    display: none;
}

.hero{
text-align:center;
padding-top:120px;
padding-bottom:80px;
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
}

.hero-desc{
font-size:18px;
color:#6b7280;
max-width:700px;
margin:auto;
margin-top:20px;
}

.icon-card{
text-align:center;
padding:40px;
border-radius:16px;
background:#f8fafc;
transition:0.25s;
cursor:pointer;
}

.icon-card:hover{
transform:translateY(-6px);
box-shadow:0px 15px 35px rgba(0,0,0,0.15);
}

.icon{
font-size:50px;
}

.icon-title{
font-size:22px;
font-weight:600;
margin-top:10px;
}

.icon-desc{
color:#6b7280;
}

.link{
text-decoration:none;
color:inherit;
}

</style>
""", unsafe_allow_html=True)

# -------- HERO --------

st.markdown("""
<div class="hero">

<div class="hero-title">
Jason <span class="hero-highlight">Sim</span>
</div>

<div class="hero-sub">
Automation Systems • Website Analytics • Data Dashboards
</div>

<div class="hero-desc">
I design automation systems and analytics dashboards that
transform operational data into insights.
</div>

</div>
""", unsafe_allow_html=True)

# -------- NAVIGATION ICONS --------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<a class="link" href="/AboutMe">
<div class="icon-card">
<div class="icon">👤</div>
<div class="icon-title">About Me</div>
<div class="icon-desc">
Background and expertise
</div>
</div>
</a>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<a class="link" href="/Experiences">
<div class="icon-card">
<div class="icon">💼</div>
<div class="icon-title">Experiences</div>
<div class="icon-desc">
Professional journey
</div>
</div>
</a>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<a class="link" href="/Projects">
<div class="icon-card">
<div class="icon">⚙️</div>
<div class="icon-title">Projects</div>
<div class="icon-desc">
Systems and dashboards built
</div>
</div>
</a>
""", unsafe_allow_html=True)

st.markdown("<br><br>")
st.caption("© Jason Sim")
