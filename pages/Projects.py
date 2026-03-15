import streamlit as st
from nav import navbar

st.set_page_config(layout="wide")

navbar()

st.title("Projects")

st.subheader("ICT Booking Automation")

st.write("""
Automated equipment booking using
Google Forms, Sheets and Apps Script.
""")

st.divider()

st.subheader("Inventory Dashboard")

st.write("""
Analytics dashboard monitoring ICT asset usage.
""")

st.divider()

st.subheader("Attendance Analytics System")

st.write("""
Excel-based system identifying attendance trends.
""")
