import streamlit as st
import pandas as pd

st.title("Interactive Dashboards")

data = pd.DataFrame({
    "Systems": ["Automation", "Dashboards", "Platforms"],
    "Projects": [10, 15, 20]
})

st.bar_chart(data.set_index("Systems"))

st.write("Example analytics dashboard visualising system development work.")
