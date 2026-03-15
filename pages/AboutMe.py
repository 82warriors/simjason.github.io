import streamlit as st

st.set_page_config(page_title="About Me", page_icon="👤", layout="wide")

st.title("About Me")

st.write("""
I am an Infocomm Technology professional passionate about building
automation systems, analytics dashboards and digital platforms that
improve operational efficiency.

My work focuses on using technology to simplify workflows,
support decision making and transform data into meaningful insights.
""")

st.subheader("What I Do")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚙️ Automation Systems")
    st.write("Design workflow automation to streamline operations.")

with col2:
    st.markdown("### 📊 Analytics Dashboards")
    st.write("Develop dashboards that support data-driven decisions.")

with col3:
    st.markdown("### 💻 ICT Digital Platforms")
    st.write("Build systems that improve digital processes.")

st.subheader("Technology")

st.write("""
Python • Streamlit • Google Apps Script  
Data Analytics • Workflow Automation  
Excel Systems • ICT Infrastructure
""")
