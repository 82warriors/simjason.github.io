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

My work focuses on building practical systems that improve workflows,
reduce manual processes, and provide better operational insights.
""")

st.button("Explore My Projects")

st.divider()

# FOCUS AREAS
st.header("Focus Areas")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚙️ Automation")
    st.write("Workflow automation and digital systems that streamline operations.")

with col2:
    st.markdown("### 📊 Dashboards")
    st.write("Data dashboards that transform raw data into clear insights.")

with col3:
    st.markdown("### 💻 ICT Systems")
    st.write("Custom ICT systems for inventory, booking, and management.")

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
- Improved equipment tracking
""")

with col2:
    st.markdown("""
### 📦 Inventory Management System

Digital asset tracking system with
analytics dashboards.

**Impact**

- Centralised equipment tracking  
- Real-time reporting  
- Improved resource management
""")

with col3:
    st.markdown("""
### 🌐 ICT Staff Portal

One-stop portal for ICT services
and staff requests.

**Impact**

- Simplified ICT processes  
- Improved staff access  
- Consolidated digital services
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

st.markdown("""
**Languages & Tools**

Python • Streamlit • Google Apps Script  
Excel Automation • Data Analytics  
Workflow Automation • ICT Infrastructure
""")

st.divider()

# CONTACT
st.header("Connect")

st.markdown("""
GitHub: https://github.com/simjason  
Website: https://simjason.com
""")

st.markdown("---")

st.caption("© Jason Sim")
