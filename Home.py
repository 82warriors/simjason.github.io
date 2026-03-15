import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="centered"
)

st.title("Jason Sim")
st.write("Technology Advocate")
st.write("Automation Systems | Website Analytics | Data Dashboards")

st.markdown("---")

# CARD STYLE
st.markdown("""
<style>

.card {
    padding:22px;
    border-radius:12px;
    border:1px solid #e6e6e6;
    text-align:center;
    background:linear-gradient(135deg,#f8f9fa,#ffffff);
    transition:0.2s;
}

.card:hover {
    transform:translateY(-4px);
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
}

.card a {
    text-decoration:none;
    color:black;
    display:block;
}

.card h3 {
    margin-bottom:5px;
}

.card p {
    font-size:14px;
    color:#666;
}

</style>
""", unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.markdown("""
<a href="AboutMe">
<div class="card">
<h3>👤 About</h3>
<p>Who I am and what I do.</p>
</div>
</a>
""", unsafe_allow_html=True)
    st.page_link("pages/AboutMe.py", label="")


with col2:
    st.markdown("""
<a href="Projects">
<div class="card">
<h3>⚙️ Projects</h3>
<p>Systems and platforms I built.</p>
</div>
</a>
""", unsafe_allow_html=True)
    st.page_link("pages/projects.py", label="")


with col3:
    st.markdown("""
<a href="Portfolio">
<div class="card">
<h3>📊 Portfolio</h3>
<p>Digital platforms and analytics work.</p>
</div>
</a>
""", unsafe_allow_html=True)
    st.page_link("pages/portfolio.py", label="")


with col4:
    st.markdown("""
<a href="Dashboard">
<div class="card">
<h3>📈 Dashboard</h3>
<p>Interactive analytics dashboard.</p>
</div>
</a>
""", unsafe_allow_html=True)
    st.page_link("pages/dashboard.py", label="")


st.markdown("---")
st.caption("© Jason Sim")
