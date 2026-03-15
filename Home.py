import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# --- STYLE ---
st.markdown("""
<style>

.hero {
    text-align:center;
    padding:120px 20px 80px 20px;
}

.hero-title {
    font-size:72px;
    font-weight:700;
}

.hero-tagline {
    font-size:24px;
    color:#6b7280;
}

.highlight {
    background: linear-gradient(120deg,#7c6cf6,#4cc9f0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.section {
    text-align:center;
    padding:40px;
    transition:0.2s;
}

.section:hover {
    transform:translateY(-4px);
}

.nav-title {
    font-size:30px;
    font-weight:600;
}

.nav-desc {
    color:#6b7280;
}

</style>
""", unsafe_allow_html=True)


# --- HERO ---
st.markdown("""
<div class="hero">
<div class="hero-title">
Jason <span class="highlight">Sim</span>
</div>

<div class="hero-tagline">
Technology Advocate • Website Analytics • Automation Systems
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# --- NAVIGATION ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
<div class="section">
<div class="nav-title">👤 About</div>
<div class="nav-desc">
Who I am and what I do
</div>
</div>
""", unsafe_allow_html=True)

    st.page_link("pages/AboutMe.py", label="Explore")


with col2:
    st.markdown("""
<div class="section">
<div class="nav-title">⚙️ Projects</div>
<div class="nav-desc">
Systems and platforms I built
</div>
</div>
""", unsafe_allow_html=True)

    st.page_link("pages/Projects.py", label="Explore")


with col3:
    st.markdown("""
<div class="section">
<div class="nav-title">💼 Experience</div>
<div class="nav-desc">
My professional journey
</div>
</div>
""", unsafe_allow_html=True)

    st.page_link("pages/Experiences.py", label="Explore")


with col4:
    st.markdown("""
<div class="section">
<div class="nav-title">📊 Dashboard</div>
<div class="nav-desc">
Interactive analytics work
</div>
</div>
""", unsafe_allow_html=True)

    st.page_link("pages/Dashboard.py", label="Explore")

st.markdown("---")

st.caption("© Jason Sim")
