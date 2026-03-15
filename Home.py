import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# STYLE
st.markdown("""
<style>

.hero {
    text-align:center;
    padding:100px 20px;
    background: linear-gradient(135deg,#7aa2ff,#8fd3f4,#a1ffce);
    border-radius:20px;
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

.nav-link {
    font-size:28px;
    font-weight:600;
    text-align:center;
    padding:40px;
    transition:0.2s;
}

.nav-link:hover {
    transform:translateY(-5px);
}

.about {color:#6c63ff;}
.projects {color:#ff7a7a;}
.experience {color:#ffb347;}
.dashboard {color:#4cd964;}

</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
<div class="hero-title">Jason Sim</div>
<div class="hero-sub">
Technology Advocate • Website Analytics • Automation Systems
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# NAVIGATION
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="nav-link about">👤 About</div>', unsafe_allow_html=True)
    st.page_link("pages/AboutMe.py", label="")

with col2:
    st.markdown('<div class="nav-link projects">⚙️ Projects</div>', unsafe_allow_html=True)
    st.page_link("pages/Projects.py", label="")

with col3:
    st.markdown('<div class="nav-link experience">💼 Experience</div>', unsafe_allow_html=True)
    st.page_link("pages/Experiences.py", label="")

with col4:
    st.markdown('<div class="nav-link dashboard">📊 Dashboard</div>', unsafe_allow_html=True)
    st.page_link("pages/Dashboard.py", label="")
