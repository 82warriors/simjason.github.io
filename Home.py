import streamlit as st

st.set_page_config(page_title="Jason Sim", page_icon="🚀", layout="wide")

st.title("Jason Sim")

st.subheader("Website Analytics | Automation Systems | Data Dashboards")

st.write("""
Digital transformation and data analytics professional with over a decade
of experience driving technology innovation and operational improvements.

Experienced in building automation systems, analytics dashboards and
web platforms that transform manual workflows into scalable digital solutions.
""")

st.divider()

st.header("Core Expertise")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌐 Website Analytics")
    st.write("Analyse website traffic, engagement metrics and user behaviour.")

with col2:
    st.markdown("### ⚙️ Automation Systems")
    st.write("Develop workflow automation using Google Apps Script.")

with col3:
    st.markdown("### 📊 Data Dashboards")
    st.write("Build operational dashboards to support decision making.")

st.divider()

st.header("Featured Projects")

st.write("""
• ICT Booking Automation System  
• ICT Inventory Microsite  
• Operational Data Dashboards
""")
