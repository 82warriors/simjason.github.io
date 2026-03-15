import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# HERO
st.markdown("""
<h1 style='text-align:center;font-size:64px;'>Jason Sim</h1>
<p style='text-align:center;font-size:22px;color:#666;'>
Technology Advocate • Website Analytics • Automation Systems
</p>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# CARD STYLE
st.markdown("""
<style>

.card {
    padding:40px;
    border-radius:28px;
    background:#f5f5f5;
    box-shadow:0px 10px 25px rgba(0,0,0,0.08);
    transition:all 0.3s ease;
    margin-bottom:40px;
    position:relative;
    overflow:hidden;
}

/* gradient hover glow */
.card::before {
    content:'';
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:linear-gradient(120deg,#7aa2ff,#8fd3f4,#a1ffce);
    opacity:0;
    transition:0.3s;
}

.card:hover::before {
    opacity:0.15;
}

.card:hover {
    transform:translateY(-8px);
    box-shadow:0px 25px 50px rgba(0,0,0,0.2);
}

/* icon animation */
.card-icon {
    font-size:42px;
    margin-bottom:10px;
    transition:0.3s;
}

.card:hover .card-icon {
    transform:scale(1.15) rotate(4deg);
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


# RESPONSIVE GRID (2 columns)
col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.page_link("pages/AboutMe.py", label="")

    st.markdown("""
<div class="card-icon">👤</div>
<div class="card-title">About Me</div>
<div class="card-desc">
Learn about my background, experience and technology journey.
</div>
""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)



    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.page_link("pages/Experiences.py", label="")

    st.markdown("""
<div class="card-icon">💼</div>
<div class="card-title">Experience</div>
<div class="card-desc">
Professional experience leading ICT initiatives and digital transformation.
</div>
""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)



with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.page_link("pages/Projects.py", label="")

    st.markdown("""
<div class="card-icon">⚙️</div>
<div class="card-title">Projects</div>
<div class="card-desc">
Automation systems, dashboards and digital platforms I have built.
</div>
""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)



    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.page_link("pages/Dashboard.py", label="")

    st.markdown("""
<div class="card-icon">📊</div>
<div class="card-title">Dashboard</div>
<div class="card-desc">
Interactive analytics dashboards and data visualisations.
</div>
""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
