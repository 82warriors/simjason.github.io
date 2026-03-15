import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>

.hero {
    text-align:center;
    padding:140px 20px 100px 20px;
    background: linear-gradient(120deg,#7c6cf6,#4cc9f0,#72efdd);
    border-radius:25px;
}

.hero-title {
    font-size:72px;
    font-weight:700;
    color:white;
}

.hero-sub {
    font-size:26px;
    color:white;
}

.nav-box {
    text-align:center;
    padding:40px;
    border-radius:20px;
    background:#f9fafb;
    transition:0.25s;
}

.nav-box:hover {
    transform:translateY(-6px);
    box-shadow:0px 12px 30px rgba(0,0,0,0.15);
}

.nav-title {
    font-size:28px;
    font-weight:600;
}

.nav-desc {
    color:#6b7280;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)


# ---------- HERO ----------
st.markdown("""
<div class="hero">

<div class="hero-title">
Jason Sim
</div>

<div class="hero-sub">
Technology Advocate • Website Analytics • Automation Systems
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)


# ---------- NAVIGATION ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
<div class="nav-box">
<div class="nav-title">👤 About</div>
<div class="nav-desc">
Who I am and what I do
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/AboutMe.py", label="Explore")


with col2:
    st.markdown("""
<div class="nav-box">
<div class="nav-title">⚙️ Projects</div>
<div class="nav-desc">
Systems and platforms I built
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/Projects.py", label="Explore")


with col3:
    st.markdown("""
<div class="nav-box">
<div class="nav-title">💼 Experience</div>
<div class="nav-desc">
Professional journey
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/Experiences.py", label="Explore")


with col4:
    st.markdown("""
<div class="nav-box">
<div class="nav-title">📊 Dashboard</div>
<div class="nav-desc">
Interactive analytics work
</div>
</div>
""", unsafe_allow_html=True)
    st.page_link("pages/Dashboard.py", label="Explore")


st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© Jason Sim")
