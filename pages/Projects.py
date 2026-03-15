import streamlit as st
from nav import navbar

st.set_page_config(layout="wide")

navbar()

st.title("Projects")

st.subheader("ICT Booking Automation")

st.write("""
Automated equipment booking workflow using
Google Forms, Sheets and Apps Script.

Impact
• Reduced manual coordination
• Enabled real-time resource tracking
""")

st.divider()

st.subheader("ICT Inventory Dashboard")

st.write("""
Dashboard analysing ICT asset usage and inventory data.

Impact
• Centralised equipment tracking
• Improved reporting visibility
""")

st.divider()

st.subheader("Late Coming Monitoring System")

st.write("""
Excel-based analytics system analysing attendance trends.

Impact
• Automated reports
• Identified behavioural patterns
""")
