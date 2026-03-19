import streamlit as st
from nav import navbar

st.set_page_config(page_title="About - Jason Sim", layout="wide")

navbar()

st.title("About Me")

st.write("""
I am an ICT professional with experience in managing infrastructure, developing automation solutions, 
and building digital systems within the education sector.

My work focuses on improving operational workflows through automation, dashboards, and user-friendly systems.
""")

st.header("Core Strengths")

col1, col2 = st.columns(2)

with col1:
    st.write("""
    • Automation (Google Apps Script, Excel)  
    • Web Development (HTML, JavaScript)  
    """)

with col2:
    st.write("""
    • Data Analysis & Dashboards  
    • ICT Infrastructure Management  
    """)

st.header("What I Focus On")

st.write("""
- Streamlining processes through automation  
- Building systems that reduce manual workload  
- Creating dashboards for better decision-making  
""")
