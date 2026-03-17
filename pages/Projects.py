import streamlit as st
from nav import navbar

st.set_page_config(
    page_title="Projects | Jason Sim",
    page_icon="📂",
    layout="wide"
)

# Navbar
navbar()

# ---------- STYLE ----------
st.markdown("""
<style>

.section-title{
    margin-top:20px;
    color:#6366F1;
    font-size:36px;
    font-weight:700;
}

.project-card{
    padding:25px;
    border-radius:16px;
    background: linear-gradient(145deg,#ffffff,#f1f5f9);
    border:1px solid #e5e7eb;
    transition:0.3s;
}

.project-card:hover{
    transform:translateY(-6px);
    box-shadow:0px 10px 30px rgba(0,0,0,0.1);
}

.tag{
    display:inline-block;
    padding:6px 12px;
    margin:4px 4px 0 0;
    background:#EEF2FF;
    color:#4F46E5;
    border-radius:999px;
    font-size:12px;
}

.center{
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="section-title">🚀 My Projects</div>', unsafe_allow_html=True)

st.markdown("""
Explore selected projects focusing on automation, analytics and ICT systems development.
""")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- PROJECT DATA ----------
projects = [
    {
        "title": "ICT Equipment Booking System",
        "desc": "Automated booking workflow with approval system and email notifications.",
        "tags": ["Automation", "Google Apps Script", "Workflow"],
        "link": "#"
    },
    {
        "title": "ICT Inventory Dashboard",
        "desc": "Interactive dashboard tracking assets, faults and operational data.",
        "tags": ["Analytics", "Dashboard", "Data Visualisation"],
        "link": "#"
    },
    {
        "title": "Attendance Analytics System",
        "desc": "Excel-based analytics solution to track attendance trends and insights.",
        "tags": ["Excel", "Data Analysis", "Reporting"],
        "link": "#"
    },
    {
        "title": "ICT Microsite Portal",
        "desc": "Centralised portal for staff to access ICT services and resources.",
        "tags": ["Web", "User Experience", "Portal"],
        "link": "#"
    },
]

# ---------- DISPLAY PROJECTS ----------
cols = st.columns(2)

for i, project in enumerate(projects):

    with cols[i % 2]:

        tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in project["tags"]])

        st.markdown(f"""
<div class="project-card">
    <h3>{project["title"]}</h3>
    <p>{project["desc"]}</p>
    {tags_html}
    <br><br>
</div>
""", unsafe_allow_html=True)

        st.link_button("🔍 View Details", project["link"])

        st.markdown("<br>", unsafe_allow_html=True)


# ---------- FOOTER ----------
st.divider()

st.markdown("""
<div class="center">
<p>More projects coming soon 🚀</p>
</div>
""", unsafe_allow_html=True)
