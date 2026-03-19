import streamlit as st
from nav import navbar

st.set_page_config(page_title="Projects - Jason Sim", layout="wide")

navbar()

st.title("Projects")

# ---------- PROJECT 1 ----------
st.subheader("📦 Inventory Management System")

st.write("""
A web-based system for managing ICT assets, fault reporting, and patching status.
""")

st.markdown("**Key Features**")
st.write("""
• CSV upload and data handling  
• Fault tracking system  
• Patching reports with auto calculations  
""")

st.markdown("**Tools**")
st.write("HTML, JavaScript, GitHub Pages")

st.markdown("**Impact**")
st.write("Improved asset visibility and reduced manual tracking.")

st.divider()

# ---------- PROJECT 2 ----------
st.subheader("⚙️ Automation Workflow System")

st.write("""
Automated booking and approval workflows using Google Apps Script.
""")

st.markdown("**Key Features**")
st.write("""
• Email notifications  
• Approval system  
• Booking tracking  
""")

st.markdown("**Tools**")
st.write("Google Apps Script, Google Sheets")

st.markdown("**Impact**")
st.write("Reduced administrative workload and improved efficiency.")

st.divider()

# ---------- PROJECT 3 ----------
st.subheader("📊 Data Dashboard")

st.write("""
Interactive dashboards for reporting and operational analysis.
""")

st.markdown("**Key Features**")
st.write("""
• Real-time data summaries  
• Visual dashboards  
• Automated reporting  
""")

st.markdown("**Tools**")
st.write("Excel, Google Sheets")

st.markdown("**Impact**")
st.write("Enabled faster decision-making and reporting.")
