import streamlit as st

def navbar():

    st.markdown("""
    <style>

    [data-testid="stSidebar"] {display:none;}

    .logo{
        font-size:26px;
        font-weight:700;
        background: linear-gradient(90deg,#6366F1,#4CC9F0);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }

    .nav{
        padding-bottom:20px;
        border-bottom:1px solid #eee;
    }

    .menu a{
        text-decoration:none;
        font-weight:500;
        color:#111827;
    }

    .menu a:hover{
        color:#6366F1;
    }

    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([6,4])

    with col1:
        st.markdown('<div class="logo">Jason Sim</div>', unsafe_allow_html=True)

    with col2:

        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.page_link("Home.py", label="Home")

        with c2:
            st.page_link("pages/AboutMe.py", label="About")

        with c3:
            st.page_link("pages/Experiences.py", label="Experiences")

        with c4:
            st.page_link("pages/Projects.py", label="Projects")
