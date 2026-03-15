import streamlit as st

st.set_page_config(page_title="Jason Sim", layout="wide")

st.title("Jason Sim")

st.subheader("Digital Systems Builder")

st.write("""
I design systems that simplify work through automation,
data dashboards and digital workflows.
""")

st.divider()

st.header("What I Build")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Automation Systems", "10+")

with col2:
    st.metric("Dashboards", "15+")

with col3:
    st.metric("ICT Solutions", "20+")

st.divider()

st.header("Featured Projects")

st.write("🔹 ICT Equipment Booking System")
st.write("🔹 Inventory Management Dashboard")
st.write("🔹 ICT Staff Portal")
