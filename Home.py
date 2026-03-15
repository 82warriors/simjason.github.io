import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# HERO
st.markdown("""
<h1 style='text-align:center;font-size:60px;'>Jason Sim</h1>
<p style='text-align:center;font-size:22px;color:#666;'>
Technology Advocate • Website Analytics • Automation Systems
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# CARD STYLE
st.markdown("""
<style>

.card {
    padding:35px;
    border-radius:24px;
    background:#f3f3f3;
    box-shadow:0px 8px 20px rgba(0,0,0,0.08);
    transition:0.25s;
    margin-bottom:25px;
}

.card:hover {
    transform:translateY(-6px);
    box-shadow:0px 16px 35px rgba(0,0,0,0.15);
}

.card-title {
    font-size:32px;
    font-weight:700;
    margin-bottom:10px;
}

.card-desc {
    font-size:18px;
    color:#666;
}

</style>
""", unsafe_allow_html=True)


# CARD 1
st.markdown('<div class="card">', unsafe_allow_html=True)

st.page_link(
    "pages/AboutMe.py",
    label="About Me"
)

st.markdown("""
<div class="card-title">
About Me
</div>
<div class="card-desc">
Learn about my background, experience and technology journey.
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# CARD 2
st.markdown('<div class="card">', unsafe_allow_html=True)

st.page_link(
    "pages/Projects.py",
    label="Projects"
)

st.markdown("""
<div class="card-title">
Projects
</div>
<div class="card-desc">
Automation systems, dashboards and digital platforms I have built.
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# CARD 3
st.markdown('<div class="card">', unsafe_allow_html=True)

st.page_link(
    "pages/Experiences.py",
    label="Experience"
)

st.markdown("""
<div class="card-title">
Experience
</div>
<div class="card-desc">
Professional work leading ICT initiatives and digital transformation.
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# CARD 4
st.markdown('<div class="card">', unsafe_allow_html=True)

st.page_link(
    "pages/Dashboard.py",
    label="Dashboard"
)

st.markdown("""
<div class="card-title">
Dashboard
</div>
<div class="card-desc">
Interactive analytics dashboards and data visualisations.
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
