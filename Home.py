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
I build digital systems that simplify work, automate workflows,
and transform data into meaningful insights.

My work focuses on automation, dashboards, and ICT systems
that improve operational efficiency.
""")

st.divider()

# WHAT I BUILD
st.header("What I Build")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("⚙️ Automation")
    st.write("Workflow automation using Google Apps Script and Python.")

with col2:
    st.subheader("📊 Dashboards")
    st.write("Data dashboards for operational insights and reporting.")

with col3:
    st.subheader("💻 ICT Systems")
    st.write("Custom systems for inventory, booking, and management.")

st.divider()

# FEATURED PROJECTS
st.header("Featured Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("ICT Equipment Booking System")
    st.write("""
    Automated booking workflow for staff equipment requests.

    **Impact**
    - Reduced manual coordination
    - Automated approval notifications
    - Improved booking visibility
    """)

with col2:
    st.subheader("Inventory Management Dashboard")
    st.write("""
    Digital asset tracking system with analytics dashboards.

    **Impact**
    - Centralised inventory tracking
    - Real-time equipment insights
    - Improved resource management
    """)

st.divider()

# TECH STACK
st.header("Technology Stack")

st.write("""
Python • Streamlit • Google Apps Script • Excel Automation  
Data Analytics • Workflow Automation • ICT Systems
""")

st.divider()

st.success("Explore the sidebar to learn more about my projects and beliefs.")
