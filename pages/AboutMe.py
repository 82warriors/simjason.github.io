import streamlit as st
import os
from nav import navbar

st.set_page_config(
    page_title="About Me | Jason Sim",
    page_icon="👋",
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

.about-text{
    font-size:18px;
    color:#374151;
    line-height:1.6;
}

.highlight{
    color:#6366F1;
    font-weight:600;
}

.skill-card{
    padding:20px;
    border-radius:14px;
    background:#F8FAFC;
    border:1px solid #e5e7eb;
    text-align:center;
    transition:0.3s;
}

.skill-card:hover{
    transform:translateY(-5px);
    box-shadow:0px 8px 20px rgba(0,0,0,0.08);
}

.skill-icon{
    font-size:30px;
}

.skill-title{
    margin-top:10px;
    font-weight:600;
}

.center{
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="section-title">👋 About Me</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- INTRO ----------
col1, col2 = st.columns([2,1])

with col1:

    st.markdown("""
<div class="about-text">

Hi, I’m <span class="highlight">Jason Sim</span> — an ICT professional specialising in 
automation systems, analytics dashboards and digital solutions.

I focus on building systems that <span class="highlight">reduce manual work</span>, 
<span class="highlight">improve efficiency</span>, and turn operational data into 
meaningful insights.

With experience in the education sector, I have worked on developing 
automation workflows, managing ICT infrastructure, and designing web-based systems 
to support staff and organisational operations.

</div>
""", unsafe_allow_html=True)

with col2:
    image_path = os.path.join("images", "jason.png")
    st.image(image_path, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------- WHAT I DO ----------
st.markdown('<div class="section-title">🚀 What I Do</div>', unsafe_allow_html=True)

st.markdown("""
<div class="about-text">
I bridge the gap between operations and technology by designing systems that are 
both practical and scalable.

My work revolves around:
</div>
""", unsafe_allow_html=True)

st.markdown("""
- ⚙️ Automation of workflows and processes  
- 📊 Data analytics and dashboard development  
- 🌐 Building web-based systems and internal portals  
- 🖥️ Managing ICT infrastructure and digital environments  
""")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- SKILLS ----------
st.markdown('<div class="section-title">🧠 Skills</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
<div class="skill-card">
<div class="skill-icon">⚙️</div>
<div class="skill-title">Automation</div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="skill-card">
<div class="skill-icon">📊</div>
<div class="skill-title">Analytics</div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="skill-card">
<div class="skill-icon">🌐</div>
<div class="skill-title">Web Systems</div>
</div>
""", unsafe_allow_html=True)

with col4:
    st.markdown("""
<div class="skill-card">
<div class="skill-icon">🖥️</div>
<div class="skill-title">ICT Infrastructure</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------- PERSONAL TOUCH ----------
st.markdown('<div class="section-title">💡 My Approach</div>', unsafe_allow_html=True)

st.markdown("""
<div class="about-text">

I believe technology should not complicate work — it should simplify it.

My approach is to design solutions that are:
<br><br>
✔️ Practical and easy to use  
✔️ Scalable for future needs  
✔️ Focused on real operational impact  

I enjoy solving problems, optimising workflows, and building systems that make 
everyday processes smoother and more efficient.

</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.divider()

st.markdown("""
<div class="center">
<p>Always building. Always improving 🚀</p>
</div>
""", unsafe_allow_html=True)
