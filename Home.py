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

st.markdown("### Explore")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.page_link("pages/AboutMe.py", label="About")

with col2:
    st.page_link("pages/projects.py", label="Projects")

with col3:
    st.page_link("pages/portfolio.py", label="Portfolio")

with col4:
    st.page_link("pages/dashboard.py", label="Dashboard")

st.markdown("---")

st.caption("© Jason Sim")
