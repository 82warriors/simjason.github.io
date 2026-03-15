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

# PROJECT CARDS
st.header("Featured Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
### ⚙️ Equipment Booking System
Automated equipment booking workflow.

**Impact**
- Reduced manual coordination
- Faster approvals
""")

with col2:
    st.markdown("""
### 📦 Inventory Dashboard
Digital asset tracking system.

**Impact**
- Centralised inventory tracking
- Real-time analytics
""")

with col3:
    st.markdown("""
### 🌐 ICT Staff Portal
Centralised portal for ICT services.

**Impact**
- Simplified staff requests
- Improved access to resources
""")

st.divider()

st.markdown("© Jason Sim")
