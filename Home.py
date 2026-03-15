import streamlit as st

st.set_page_config(page_title="Jason Sim", page_icon="🚀", layout="centered")

st.title("Jason Sim")
st.write("Technology Advocate")
st.write("Automation Systems | Website Analytics | Data Dashboards")

st.markdown("---")

# MODERN CARD STYLE
st.markdown("""
<style>

.card {
    padding:25px;
    border-radius:12px;
    border:1px solid #e6e6e6;
    background-color:white;
    transition: all 0.2s ease;
    height:160px;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
}

.card a {
    text-decoration:none;
    color:black;
}

.card-title {
    font-size:22px;
    font-weight:600;
    margin-bottom:8px;
}

.card-desc {
    font-size:14px;
    color:#555;
}

</style>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.markdown("""
<a href="?page=AboutMe">
<div class="card">
<div class="card-title">👤 About</div>
<div class="card-desc">
Learn more about my background, experience,
and areas of expertise.
</div>
</div>
</a>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<a href="?page=projects">
<div class="card">
<div class="card-title">⚙️ Projects</div>
<div class="card-desc">
Explore automation systems, digital platforms
and analytics solutions I have built.
</div>
</div>
</a>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<a href="?page=portfolio">
<div class="card">
<div class="card-title">📊 Portfolio</div>
<div class="card-desc">
View my digital platforms, website analytics
and operational technology initiatives.
</div>
</div>
</a>
""", unsafe_allow_html=True)

with col4:
    st.markdown("""
<a href="?page=dashboard">
<div class="card">
<div class="card-title">📈 Dashboard</div>
<div class="card-desc">
Interactive analytics dashboard showing
data visualisation and reporting capabilities.
</div>
</div>
</a>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("© Jason Sim")
