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
BASE_URL = "https://docs.google.com/spreadsheets/d/1x4EP6dO3FpkFRMBXqHDku0pl4vtHrWnE1S3J-e86vt0/export?format=csv&gid="

# 🔥 TARGET MODELS
TARGET_MODELS = [
    "ACER VX2670G DESKTOP",
    "LENOVO K14 GEN2",
    "LENOVO L13 YOGA G4"
]

# ==================================================
# LOAD DATA (AUTO DETECT HEADER)
# ==================================================
@st.cache_data(ttl=120)
def load_data(gid):
    url = BASE_URL + gid

    raw = pd.read_csv(url, header=None, dtype=str)

    header_row = None

    for i in range(len(raw)):
        row = raw.iloc[i].astype(str).str.upper()

        if "BRANDMODEL" in row.values or "MODEL" in row.values:
            header_row = i
            break

    if header_row is None:
        st.error("❌ Header not found")
        st.stop()

    df = pd.read_csv(url, header=header_row)

    df.columns = df.columns.astype(str).str.strip()
    df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]

    return df

# ==================================================
# 🔥 USE LATEST SHEET (MANUAL GID FOR NOW)
# ==================================================
# 👉 Replace if you want auto-detect across sheets
LATEST_GID = "1946114847"

df = load_data(LATEST_GID)

# ==================================================
# CLEAN DATA
# ==================================================
# Normalize BrandModel
if "BrandModel" in df.columns:
    df["BrandModel"] = df["BrandModel"].astype(str).str.upper().str.strip()

# Normalize Status column
STATUS_COL = None

for col in df.columns:
    if "STATUS" in col.upper():
        STATUS_COL = col
        break

if STATUS_COL is None:
    st.error("❌ No Status column found")
    st.write("Detected columns:", df.columns.tolist())
    st.stop()

# ==================================================
# FILTER TARGET MODELS
# ==================================================
df_filtered = df[df["BrandModel"].isin(TARGET_MODELS)]

# ==================================================
# COMPUTE STATUS
# ==================================================
summary = (
    df_filtered
    .groupby(["BrandModel", STATUS_COL])
    .size()
    .unstack(fill_value=0)
)

# Ensure columns exist
for col in ["Completed", "Not Completed"]:
    if col not in summary.columns:
        summary[col] = 0

summary = summary.reset_index()

# ==================================================
# KPI
# ==================================================
st.markdown("## 📊 Overview")

total_completed = summary["Completed"].sum()
total_not_completed = summary["Not Completed"].sum()

c1, c2 = st.columns(2)

c1.metric("✅ Completed", int(total_completed))
c2.metric("❌ Not Completed", int(total_not_completed))

# ==================================================
# TABLE
# ==================================================
st.markdown("## 📋 Upgrade Summary")

st.dataframe(summary, use_container_width=True, hide_index=True)

# ==================================================
# BAR CHART
# ==================================================
st.markdown("## 📈 Upgrade Progress")

chart_df = summary.set_index("BrandModel")[["Completed", "Not Completed"]]

st.bar_chart(chart_df)

# ==================================================
# RAW DATA
# ==================================================
with st.expander("🔍 View Raw Data"):
    st.dataframe(df_filtered, use_container_width=True)
