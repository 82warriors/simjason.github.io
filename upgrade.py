import streamlit as st
import pandas as pd

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(page_title="Upgrade Tracking", layout="wide")

st.title("⬆️ Upgrade Status Dashboard")

# ==================================================
# CONFIG
# ==================================================
BASE_URL = "https://docs.google.com/spreadsheets/d/1x4EP6dO3FpkFRMBXqHDku0pl4vtHrWnE1S3J-e86vt0/export?format=csv&gid=1946114847"

TARGET_MODELS = [
    "ACER VX2670G DESKTOP",
    "LENOVO K14 GEN2",
    "LENOVO L13 YOGA G4"
]

# ==================================================
# LOAD DATA (BULLETPROOF)
# ==================================================
@st.cache_data(ttl=120)
def load_data():
    raw = pd.read_csv(BASE_URL, header=None, dtype=str)

    header_row = None

    for i in range(len(raw)):
        row = raw.iloc[i].astype(str).str.upper()

        if "BRANDMODEL" in row.values or "MODEL" in row.values:
            header_row = i
            break

    if header_row is None:
        st.error("❌ Cannot detect header row")
        st.stop()

    df = pd.read_csv(BASE_URL, header=header_row)

    df.columns = df.columns.astype(str).str.strip()
    df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]

    return df


df = load_data()

# ==================================================
# CLEAN DATA
# ==================================================
if "BrandModel" in df.columns:
    df["BrandModel"] = df["BrandModel"].astype(str).str.upper().str.strip()

# Detect status column
status_col = None
for col in df.columns:
    if "STATUS" in col.upper():
        status_col = col
        break

if status_col is None:
    st.error("❌ No Status column found")
    st.write(df.columns.tolist())
    st.stop()

# ==================================================
# FILTER TARGET MODELS
# ==================================================
df = df[df["BrandModel"].isin(TARGET_MODELS)]

# Normalize status values
df[status_col] = df[status_col].astype(str).str.strip().str.title()

# ==================================================
# SUMMARY
# ==================================================
summary = (
    df.groupby(["BrandModel", status_col])
    .size()
    .unstack(fill_value=0)
)

for col in ["Completed", "Not Completed"]:
    if col not in summary.columns:
        summary[col] = 0

summary = summary.reset_index()

# ==================================================
# KPI
# ==================================================
st.markdown("## 📊 Overview")

c1, c2 = st.columns(2)

c1.metric("✅ Completed", int(summary["Completed"].sum()))
c2.metric("❌ Not Completed", int(summary["Not Completed"].sum()))

# ==================================================
# TABLE
# ==================================================
st.markdown("## 📋 Upgrade Summary")

st.dataframe(summary, use_container_width=True, hide_index=True)

# ==================================================
# CHART
# ==================================================
st.markdown("## 📈 Upgrade Progress")

chart_df = summary.set_index("BrandModel")[["Completed", "Not Completed"]]
st.bar_chart(chart_df)

# ==================================================
# RAW DATA
# ==================================================
with st.expander("🔍 Raw Data"):
    st.dataframe(df, use_container_width=True)
