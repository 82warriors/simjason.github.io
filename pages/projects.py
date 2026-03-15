import streamlit as st

st.title("Projects")

st.write("A selection of digital systems, dashboards and automation solutions I have built.")

st.markdown("---")

# PROJECT 1
st.subheader("⚙️ ICT Booking Automation System")

col1, col2 = st.columns([2,1])

with col1:
    st.write("""
Developed an automated ICT equipment booking system using  
**Google Forms, Google Sheets and Google Apps Script**.

This system streamlined equipment booking workflows
and automated approval notifications.
    
**Key Features**
- Automated booking approvals
- Email notifications
- Real-time equipment tracking
- Data collection for usage analysis

**Impact**
- Reduced manual coordination
- Improved booking visibility
- Enabled data-driven resource management
""")

with col2:
    st.info("Tech Stack\n\nGoogle Forms\nGoogle Sheets\nApps Script")

st.markdown("---")


# PROJECT 2
st.subheader("📦 ICT Inventory Microsite")

col1, col2 = st.columns([2,1])

with col1:
    st.write("""
Developed a web-based ICT inventory platform to centralise
equipment records and operational reporting.

The microsite allows staff to quickly access inventory
information and improves transparency of ICT resources.

**Key Features**
- Centralised asset records
- Web-based access to inventory
- Integration with operational reports

**Impact**
- Improved accessibility of ICT information
- Better asset tracking and management
""")

with col2:
    st.info("Tech Stack\n\nGoogle Sites\nGitHub Pages\nGoogle Sheets")

st.markdown("---")


# PROJECT 3
st.subheader("📊 Inventory Analytics Dashboard")

col1, col2 = st.columns([2,1])

with col1:
    st.write("""
Developed an analytics dashboard to monitor ICT asset usage
and operational trends.

The dashboard provides insights into equipment usage,
inventory status and operational reporting.

**Key Features**
- Data visualisation of ICT resources
- Operational analytics reporting
- Dashboard insights for decision making

**Impact**
- Improved visibility of ICT assets
- Data-driven operational planning
""")

with col2:
    st.info("Tech Stack\n\nExcel\nGoogle Sheets\nData Visualisation")

st.markdown("---")


# PROJECT 4
st.subheader("🎓 MTD301 Digital Media Project")

st.write("""
Developed as part of the **Bachelor of Science in Digital Media (SUSS)**.

This project explores digital media production and platform development.

**Focus Areas**

- Digital media production
- Content development
- Digital platform engagement
""")

st.video("https://youtu.be/x1K_XMqK05o")

st.markdown("---")


# PROJECT 5
st.subheader("📈 Late Coming Monitoring System")

st.write("""
Developed an Excel-based monitoring system to analyse
student attendance trends.

The system automates data analysis and reporting
for school administration.

**Key Features**

- Attendance trend analysis
- Automated reporting
- Data insights for administration

**Impact**

- Improved monitoring of attendance patterns
- Faster reporting for school management
""")
