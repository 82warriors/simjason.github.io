import streamlit as st

st.set_page_config(page_title="Jason Sim", layout="wide")

# Hide sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display:none}
.hero {text-align:center;padding-top:120px;padding-bottom:80px;}
.hero-title {font-size:64px;font-weight:700;}
.hero-highlight {
background: linear-gradient(90deg,#6366f1,#4cc9f0);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;}
.hero-sub {font-size:24px;color:#6b7280;}
.hero-desc {font-size:18px;color:#6b7280;max-width:700px;margin:auto;margin-top:20px;}

.section-title {text-align:center;font-size:32px;font-weight:600;margin-top:60px;}

.card {
padding:30px;
border-radius:16px;
background:#f8fafc;
transition:0.25s;
text-align:center;
}

.card:hover {
transform:translateY(-6px);
box-shadow:0px 15px 35px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
<div class="hero-title">
Jason <span class="hero-highlight">Sim</span>
</div>

<div class="hero-sub">
Automation Systems • Website Analytics • Data Dashboards
</div>

<div class="hero-desc">
I build digital systems and analytics dashboards that
transform operational data into actionable insights.
</div>
</div>
""", unsafe_allow_html=True)


# WHAT I DO
st.markdown('<div class="section-title">What I Do</div>', unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">
<h3>⚙️ Automation</h3>
<p>Workflow automation systems that improve efficiency.</p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<h3>📊 Analytics</h3>
<p>Data dashboards that support operational insights.</p>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">
<h3>💻 Digital Systems</h3>
<p>ICT platforms that simplify processes and reporting.</p>
</div>
""", unsafe_allow_html=True)


# FEATURED WORK
st.markdown('<div class="section-title">Featured Work</div>', unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">
<h3>ICT Booking Automation</h3>
<p>Automated equipment booking and approval workflow.</p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<h3>Inventory Dashboard</h3>
<p>Analytics dashboard monitoring ICT asset usage.</p>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">
<h3>MTD301 Media Project</h3>
<p>Digital media storytelling and engagement project.</p>
</div>
""", unsafe_allow_html=True)


# EXPLORE
st.markdown('<div class="section-title">Explore</div>', unsafe_allow_html=True)

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
