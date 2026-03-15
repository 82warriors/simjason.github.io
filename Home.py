import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# HERO SECTION
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
    text-align:center;
}

div[data-testid="stPageLink"]:hover {
    transform:translateY(-6px);
    box-shadow:0px 10px 25px rgba(0,0,0,0.15);
}

div[data-testid="stPageLink"] a {
    font-size:22px;
    font-weight:600;
    text-decoration:none;
}

</style>
""", unsafe_allow_html=True)

# GRID CARDS
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.page_link(
        "pages/AboutMe.py",
        label="👤 About",
        help="Learn about my background and experience"
    )

with col2:
    st.page_link(
        "pages/Projects.py",
        label="⚙️ Projects",
        help="Systems, automation tools and digital platforms"
    )

with col3:
    st.page_link(
        "pages/Experiences.py",
        label="💼 Experience",
        help="Professional experience and achievements"
    )

with col4:
    st.page_link(
        "pages/Dashboard.py",
        label="📊 Dashboard",
        help="Interactive analytics and data visualisations"
    )

st.markdown("---")
st.caption("© Jason Sim")
