import streamlit as st

st.set_page_config(page_title="Jason Sim", page_icon="🚀", layout="centered")

st.title("Jason Sim")
st.write("Technology Advocate")
st.write("Automation Systems | Website Analytics | Data Dashboards")

st.markdown("---")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.markdown("### 👤 About")
    st.write("Learn more about my background and experience.")

    if st.button("Open About"):
        st.switch_page("pages/AboutMe.py")


with col2:
    st.markdown("### ⚙️ Projects")
    st.write("Systems and automation platforms I built.")

    if st.button("Open Projects"):
        st.switch_page("pages/projects.py")


with col3:
    st.markdown("### 📊 Portfolio")
    st.write("Digital platforms and analytics work.")

    if st.button("Open Portfolio"):
        st.switch_page("pages/portfolio.py")


with col4:
    st.markdown("### 📈 Dashboard")
    st.write("Interactive analytics dashboards.")

    if st.button("Open Dashboard"):
        st.switch_page("pages/dashboard.py")

st.markdown("---")
st.caption("© Jason Sim")
