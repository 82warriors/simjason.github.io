import streamlit as st
import pandas as pd

st.title("Analytics Dashboard")

data = pd.DataFrame({
    "Metric": ["Page Views", "Users", "Engagement Rate", "Bounce Rate"],
    "Value": [12000, 4200, 65, 38]
})

st.bar_chart(data.set_index("Metric"))

st.write("""
Example analytics dashboard visualising
website engagement metrics.
""")
