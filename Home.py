import streamlit as st
from nav import navbar

st.set_page_config(layout="wide")

navbar()

st.markdown("""
<style>

.hero-title{
font-size:60px;
font-weight:700;
background: linear-gradient(90deg,#6366F1,#4CC9F0);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.hero-sub{
font-size:22px;
color:#6B7280;
}

.card{
padding:25px;
border-radius:14px;
background:#F8FAFC;
transition:0.2s;
}

.card:hover{
transform:translateY(-5px);
box-shadow:0px 10px 30px rgba(0,0,0,0.1);
}

.section-title{
color:#6366F1;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-title">Automation Systems & Data Analytics</div>', unsafe_allow_html=True)

st.markdown('<div class="hero-sub">Jason Sim</div>', unsafe_allow_html=True)

st.write("""
I build automation systems, analytics dashboards and digital platforms
that transform operational data into actionable insights.
""")

st.divider()

st.markdown('<h2 class="section-title">What I Do</h2>', unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">
<h3>⚙️ Automation</h3>
<p>Workflow automation systems improving efficiency.</p>
</div>
""",unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<h3>📊 Analytics</h3>
<p>Dashboards delivering operational insights.</p>
</div>
""",unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">
<h3>💻 Digital Systems</h3>
<p>ICT platforms supporting digital transformation.</p>
</div>
""",unsafe_allow_html=True)
