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
    box-shadow:0px 18px 40px rgba(0,0,0,0.15);
}

.card-title {
    font-size:32px;
    font-weight:700;
    margin-bottom:10px;
    transition:0.2s;
}

.card-desc {
    font-size:18px;
    color:#777;
    transition:0.2s;
}

.card:hover .card-title {
    color:#000;
    transform:translateY(-2px);
}

.card:hover .card-desc {
    color:#444;
}

</style>
""", unsafe_allow_html=True)


# ABOUT CARD
st.markdown('<div class="card">', unsafe_allow_html=True)

st.page_link("pages/AboutMe.py", label="")

st.markdown("""
<div class="card-title">About Me</div>
<div class="card-desc">
Learn about my background, experience and technology journey.
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# PROJECTS CARD
st.markdown('<div class="card">', unsafe_allow_html=True)

st.page_link("pages/Projects.py", label="")

st.markdown("""
<div class="card-title">Projects</div>
<div class="card-desc">
Automation systems, dashboards and digital platforms I have built.
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# EXPERIENCE CARD
st.markdown('<div class="card">', unsafe_allow_html=True)

st.page_link("pages/Experiences.py", label="")

st.markdown("""
<div class="card-title">Experience</div>
<div class="card-desc">
Professional work leading ICT initiatives and digital transformation.
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# DASHBOARD CARD
st.markdown('<div class="card">', unsafe_allow_html=True)

st.page_link("pages/Dashboard.py", label="")

st.markdown("""
<div class="card-title">Dashboard</div>
<div class="card-desc">
Interactive analytics dashboards and data visualisations.
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
