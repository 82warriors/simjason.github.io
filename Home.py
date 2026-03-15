import streamlit as st

st.set_page_config(layout="wide")

# hide sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display:none}
.hero {text-align:center;padding-top:120px;padding-bottom:80px;}
.hero-title {font-size:64px;font-weight:700;}
.hero-sub {font-size:24px;color:#6b7280;}
.hero-desc {font-size:18px;color:#6b7280;max-width:700px;margin:auto;}
.section-title {text-align:center;font-size:32px;margin-top:60px;}
.card {padding:30px;border-radius:16px;background:#f8fafc;text-align:center;}
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
<div class="hero-title">Jason Sim</div>
<div class="hero-sub">Automation Systems • Website Analytics</div>
<div class="hero-desc">
I build automation systems and analytics dashboards
that transform operational data into insights.
</div>
</div>
""", unsafe_allow_html=True)

# WHAT I DO
st.markdown('<div class="section-title">What I Do</div>', unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h3>Automation</h3></div>',unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>Analytics</h3></div>',unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h3>Digital Systems</h3></div>',unsafe_allow_html=True)

# FEATURED WORK
st.markdown('<div class="section-title">Featured Work</div>', unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h3>ICT Booking Automation</h3></div>',unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>Inventory Dashboard</h3></div>',unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h3>MTD301 Media Project</h3></div>',unsafe_allow_html=True)
