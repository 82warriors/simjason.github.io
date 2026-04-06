import streamlit as st
import pandas as pd

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(page_title="FVPS Dashboard", layout="wide")

st.title("📊 FVPS Dashboard")

# ==================================================
# LOAD DATA
# ==================================================
@st.cache_data(ttl=120)
def load_data():
    url = "https://docs.google.com/spreadsheets/d/1lmCotLUgTLJBKska2y7od2LTPT_qooIFS0_zyVnRI0A/export?format=csv"

    raw = pd.read_csv(url, header=None, dtype=str)

    header_row = None

    for i in range(len(raw)):
        row = raw.iloc[i].astype(str).str.upper()

        if "BRANDMODEL" in row.values or "BRAND MODEL" in row.values:
            header_row = i
            break

    if header_row is None:
        st.error("❌ Cannot detect header row")
        st.stop()

    df = pd.read_csv(url, header=header_row)

    df.columns = df.columns.astype(str).str.strip()
    df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]

    # Normalize
    df = df.rename(columns={
        "Brand Model": "BrandModel",
        "Equipment Type": "EquipmentType",
        "End Date": "EndDate",
        "Start Date": "StartDate"
    })

    # Clean
    if "BrandModel" in df.columns:
        df["BrandModel"] = df["BrandModel"].astype(str).str.upper().str.strip()

    if "EquipmentType" in df.columns:
        df["EquipmentType"] = df["EquipmentType"].astype(str).str.title().str.strip()

    for col in ["EndDate", "StartDate", "Last Updated"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    df = df.dropna(how="all")

    return df


df = load_data()

# ==================================================
# REFRESH
# ==================================================
if st.button("🔄 Refresh Dashboard"):
    st.cache_data.clear()
    st.rerun()

# ==================================================
# KPI
# ==================================================
today = pd.Timestamp.today()

expired = df[df["EndDate"] < today] if "EndDate" in df.columns else pd.DataFrame()
expiring = df[
    (df["EndDate"] >= today) &
    (df["EndDate"] <= today + pd.Timedelta(days=30))
] if "EndDate" in df.columns else pd.DataFrame()

st.markdown("## 📊 Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Devices", len(df))
c2.metric("Expired", len(expired))
c3.metric("Expiring (30 Days)", len(expiring))
c4.metric("Unique Models", df["BrandModel"].nunique() if "BrandModel" in df.columns else 0)

# ==================================================
# ALERT
# ==================================================
if len(expiring) > 0:
    st.warning(f"⚠️ {len(expiring)} devices expiring within 30 days")

# ==================================================
# CHARTS
# ==================================================
st.markdown("## 📈 Insights")

colA, colB = st.columns(2)

with colA:
    st.markdown("### Equipment Distribution")
    if "EquipmentType" in df.columns:
        st.bar_chart(df["EquipmentType"].value_counts())

with colB:
    st.markdown("### Expiry Timeline")
    if "EndDate" in df.columns:
        chart = (
            df.dropna(subset=["EndDate"])
            .groupby(df["EndDate"].dt.to_period("M"))
            .size()
            .sort_index()
        )
        chart.index = chart.index.astype(str)
        st.line_chart(chart)

# ==================================================
# TOP MODELS
# ==================================================
st.markdown("## 🏆 Top Equipment Models")

if "BrandModel" in df.columns:
    top = df["BrandModel"].value_counts().head(10)
    st.dataframe(top, use_container_width=True)
