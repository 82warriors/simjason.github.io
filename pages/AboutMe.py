import streamlit as st
from nav import navbar

st.set_page_config(layout="wide")

navbar()

st.title("About Me")

st.write("""
I am an Infocomm Technology professional focused on building
automation systems, analytics dashboards and digital platforms.

My work centres on simplifying workflows, improving operational
efficiency and transforming data into insights.
""")

st.markdown("### Technology")

st.write("""
Python  
Streamlit  
Google Apps Script  
Data Analytics  
ICT Infrastructure
""")
