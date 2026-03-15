import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

# HERO SECTION
st.title("Jason Sim")
st.subheader("Technology Advocate | Automation Systems")

st.write("""
Digital transformation and data analytics professional with over a decade
of experience driving technology innovation and operational improvements
in the education sector.

I design automation systems, dashboards, and ICT solutions
that transform manual workflows into scalable digital systems.
""")

st.button("Explore My Projects")

st.divider()

# FOCUS AREAS
st.header("Focus Areas")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚙️ Automation Systems")
    st.write("Workflow automation using Google Apps Script and digital systems.")

with col2:
    st.markdown("### 📊 Data Dashboards")
    st.write("Operational dashboards for analytics and decision-making.")

with col3:
    st.markdown("### 🌐 Digital Platforms")
    st.write("Web platforms, ICT portals, and digital infrastructure.")

st.divider()

# FEATURED PROJECTS
st.header("Featured Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
### ⚙️ ICT Booking Automation

Automated equipment booking workflow using  
Google Forms, Sheets, and Apps Script.

**Impact**

- Automated approval workflows  
- Real-time booking notifications  
- Improved equipment tracking
""")

with col2:
    st.markdown("""
### 📦 ICT Inventory Microsite

Developed ICT inventory system using  
Google Sites and GitHub Pages.

**Impact**

- Centralised asset information  
- Web-based operational reports  
- Improved ICT record accessibility
""")

with col3:
    st.markdown("""
### 📊 Operational Dashboards

Built Excel and Google Sheets dashboards  
to analyse ICT resource usage.

**Impact**

- Data-driven reporting  
- Operational insights  
- Resource planning
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
    st.metric("ICT Platforms", "20+")

st.divider()

# TECHNOLOGY STACK
st.header("Technology Stack")

st.markdown("""
**Programming & Automation**

Python • Google Apps Script

**Data Analytics**

Excel • Google Sheets • Dashboard Development

**Web Platforms**

Google Sites • GitHub Pages • Isomer CMS • Swiit CMS

**Digital Analytics**

Meta Insights • Engagement Analytics
""")

st.divider()

# PROFESSIONAL EXPERIENCE
st.header("Professional Experience")

st.markdown("""
**Infocomm Technology Manager | Ministry of Education**

- Lead ICT and digital initiatives supporting teaching and learning
- Develop automation solutions using Google Apps Script
- Analyse operational data and build reporting dashboards
- Manage ICT infrastructure and digital platforms
- Conduct staff training to improve digital competency
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
