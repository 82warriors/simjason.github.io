import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# -------- STYLE --------

st.markdown("""
<style>

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

.section{
text-align:center;
padding:40px;
}

.section-title{
font-size:30px;
font-weight:600;
}

.section-desc{
color:#6b7280;
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
I design automation systems and analytics dashboards
that transform operational data into insights.
</div>

</div>
""", unsafe_allow_html=True)


# -------- WHAT I DO --------

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="section">
<div class="section-title">⚙️ Automation</div>
<div class="section-desc">
Workflow automation and digital systems.
</div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="section">
<div class="section-title">📊 Analytics</div>
<div class="section-desc">
Data dashboards for operational insights.
</div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="section">
<div class="section-title">💻 ICT Systems</div>
<div class="section-desc">
Technology platforms supporting digital operations.
</div>
</div>
""", unsafe_allow_html=True)


st.markdown("<br><br>")

st.caption("© Jason Sim")
