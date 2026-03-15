import streamlit as st

st.set_page_config(
    page_title="Jason Sim",
    page_icon="🚀",
    layout="wide"
)

st.title("Jason Sim")
st.subheader("Technology Advocate | Automation Systems")

st.write("""
Digital transformation professional specialising in automation,
data dashboards, and ICT systems that improve operational efficiency.
""")

st.button("View My Projects")

st.divider()

st.header("Focus Areas")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚙️ Automation")
    st.write("Workflow automation using Google Apps Script.")

with col2:
    st.markdown("### 📊 Data Dashboards")
    st.write("Operational analytics dashboards.")

with col3:
    st.markdown("### 🌐 Digital Platforms")
    st.write("ICT portals and web systems.")

st.divider()

st.header("Featured Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/booking_system.png")
    st.markdown("### ICT Booking Automation")

with col2:
    st.image("images/inventory_dashboard.png")
    st.markdown("### ICT Inventory Microsite")

with col3:
    st.image("images/portal.png")
    st.markdown("### ICT Staff Portal")
