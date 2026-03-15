import streamlit as st
from nav import navbar

st.set_page_config(layout="wide")

navbar()

st.title("Jason Sim")

st.write("Automation Systems • Website Analytics • Data Dashboards")

st.write("""
I build automation systems, analytics dashboards and digital platforms
that transform operational data into actionable insights.
""")

st.divider()

st.subheader("What I Do")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚙️ Automation")
    st.write("Workflow automation that improves efficiency.")

with col2:
    st.markdown("### 📊 Analytics")
    st.write("Dashboards that support operational insights.")

with col3:
    st.markdown("### 💻 Digital Systems")
    st.write("ICT platforms that simplify processes.")
