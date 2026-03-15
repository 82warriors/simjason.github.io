import streamlit as st
from nav import navbar

st.set_page_config(layout="wide")

navbar()

st.markdown("""
<style>

.hero{
text-align:center;
padding-top:120px;
padding-bottom:100px;
}

.hero-title{
font-size:64px;
font-weight:700;
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
margin-top:80px;
}

.card{
padding:30px;
border-radius:12px;
background:#f9fafb;
text-align:center;
transition:0.2s;
}

.card:hover{
transform:translateY(-5px);
box-shadow:0px 10px 30px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# HERO

st.markdown("""
<div class="hero">

<div class="hero-title">
Automation Systems & Data Analytics
</div>

<div class="hero-sub">
Jason Sim
</div>

<div class="hero-desc">
I build automation systems, analytics dashboards and digital platforms
that transform operational data into actionable insights.
</div>

</div>
""", unsafe_allow_html=True)


# WHAT I DO

st.markdown("## What I Do")

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">
<h3>⚙️ Automation</h3>
<p>Workflow automation and digital processes.</p>
</div>
""",unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<h3>📊 Analytics</h3>
<p>Data dashboards for operational insights.</p>
</div>
""",unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">
<h3>💻 ICT Systems</h3>
<p>Technology platforms supporting digital operations.</p>
</div>
""",unsafe_allow_html=True)


# EXPLORE

st.markdown("## Explore")

col1,col2,col3 = st.columns(3)

with col1:
    if st.button("About Me"):
        st.switch_page("pages/AboutMe.py")

with col2:
    if st.button("Experiences"):
        st.switch_page("pages/Experiences.py")

with col3:
    if st.button("Projects"):
        st.switch_page("pages/Projects.py")
