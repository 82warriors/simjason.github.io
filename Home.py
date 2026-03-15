import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# HERO SECTION
st.markdown("""
# Jason Sim
### Digital Systems Builder

I design automation systems, dashboards, and ICT solutions  
that simplify work and improve operational efficiency.

""")

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
**Focus Areas**

⚙️ Workflow Automation  
📊 Data Dashboards  
💻 ICT Systems  
📈 Operational Analytics
""")

with col2:
    st.markdown("""
**Technology Stack**

Python  
Streamlit  
Google Apps Script  
Data Analytics  
Automation Systems
""")

st.divider()
