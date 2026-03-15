import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# HERO
st.markdown("""
<h1 style='text-align:center;font-size:64px;'>Jason Sim</h1>
<p style='text-align:center;font-size:22px;color:gray;'>
Technology Advocate • Website Analytics • Automation Systems
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# CARD STYLE
st.markdown("""
<style>

div[data-testid="stPageLink"] {
    border-radius:14px;
    border:1px solid #e6e6e6;
    padding:30px;
    background: linear-gradient(135deg,#f8f9fa,#ffffff);
    transition:0.2s;
}

div[data-testid="stPageLink"]:hover {
    transform:translateY(-6px);
    box-shadow:0px 10px 25px rgba(0,0,0,0.15);
}

.card-title {
    font-size:24px;
    font-weight:600;
}

.card-desc {
    font-size:15px;
    color:#666;
}

</style>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)
col3, col4 = st.columns(2)


# ABOUT
with col1:
    st.page_link(
        "pages/AboutMe.py",
        label="👤 About",
    )
    st.markdown('<div class="card-desc">Learn about my background, experience and technology interests.</div>', unsafe_allow_html=True)


# PROJECTS
with col2:
    st.page_link(
        "pages/Projects.py",
        label="⚙️ Projects",
    )
    st.markdown('<div class="card-desc">Explore automation systems, dashboards and digital platforms I have built.</div>', unsafe_allow_html=True)


# EXPERIENCE
with col3:
    st.page_link(
        "pages/Experiences.py",
        label="💼 Experience",
    )
    st.markdown('<div class="card-desc">Professional experience leading ICT initiatives and digital transformation.</div>', unsafe_allow_html=True)


# DASHBOARD
with col4:
    st.page_link(
        "pages/Dashboard.py",
        label="📊 Dashboard",
    )
    st.markdown('<div class="card-desc">Interactive analytics dashboards and data visualisations.</div>', unsafe_allow_html=True)


st.markdown("---")
st.caption("© Jason Sim")
