import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# HERO SECTION
st.title("Jason Sim")
st.subheader("Digital Systems Builder")

st.write("""
I design automation systems, dashboards, and ICT solutions
that simplify work and improve operational efficiency.
""")

st.divider()

# FOCUS AREAS
st.header("Focus Areas")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚙️ Automation")
    st.write("Workflow automation and digital systems.")

with col2:
    st.markdown("### 📊 Dashboards")
    st.write("Data dashboards for insights and reporting.")

with col3:
    st.markdown("### 💻 ICT Systems")
    st.write("Custom systems for management and operations.")

st.divider()

# FEATURED PROJECTS
st.header("Featured Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
### ⚙️ Equipment Booking System

Automated equipment booking workflow
with approval notifications.

**Impact**
- Reduced manual coordination  
- Faster approvals
""")

with col2:
    st.markdown("""
### 📦 Inventory Management System

Digital asset tracking system with
analytics dashboards.

**Impact**
- Centralised equipment tracking  
- Real-time reporting
""")

with col3:
    st.markdown("""
### 🌐 ICT Staff Portal

One-stop portal for ICT services
and staff requests.

**Impact**
- Simplified ICT processes  
- Improved staff access
""")

st.divider()

# TECH PORTFOLIO METRICS
st.header("Tech Portfolio")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Automation Systems", "10+")

with col2:
    st.metric("Dashboards Built", "15+")

with col3:
    st.metric("ICT Solutions", "20+")

st.divider()

# TECHNOLOGY STACK
st.header("Technology Stack")

st.write("""
Python • Streamlit • Google Apps Script  
Data Analytics • Workflow Automation  
Excel Systems • ICT Infrastructure
""")

st.divider()

# FOOTER
st.markdown("""
### Connect

GitHub: https://github.com/simjason  
Website: https://simjason.com
""")

st.markdown("© Jason Sim")
