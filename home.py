import streamlit as st
import os
from nav import navbar

st.set_page_config(page_title="Jason Sim", page_icon="🚀", layout="wide")

navbar()

# ---------- HERO ----------
col1, col2 = st.columns([2,1])

with col1:
    st.title("Jason Sim")
    st.subheader("ICT Manager • Automation Systems • Digital Solutions")

    st.write("""
    I design and build automation systems, dashboards, and digital platforms 
    that streamline operations and improve efficiency in education.
    """)

    colA, colB = st.columns(2)
    with colA:
        st.page_link("pages/projects.py", label="🚀 View Projects")
    with colB:
        st.page_link("pages/experience.py", label="💼 Experience")

with col2:
    st.image(os.path.join("images", "jason.png"), use_container_width=True)

st.divider()

# ---------- ABOUT PREVIEW ----------
st.header("About Me")

st.write("""
ICT professional specialising in automation, system development, and data-driven solutions.  
Focused on improving workflows and reducing manual processes in education environments.
""")

st.page_link("pages/about.py", label="Read more →")

st.divider()

# ---------- WHAT I DO ----------
st.header("What I Do")

col1, col2, col3 = st.columns(3)

col1.metric("⚙️ Automation", "Workflows & Systems")
col2.metric("📊 Data", "Dashboards & Reporting")
col3.metric("💻 ICT", "Infrastructure & Platforms")

st.divider()

# ---------- PROJECT PREVIEW ----------
st.header("Featured Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("Inventory Management System")

with col2:
    st.info("Automation Workflow System")

with col3:
    st.info("Data Dashboard")

st.page_link("pages/projects.py", label="View All Projects →")

st.divider()

st.caption("© 2026 Jason Sim • ICT & Automation Portfolio")
