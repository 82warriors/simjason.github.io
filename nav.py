import streamlit as st

def navbar():

    # hide sidebar
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {display:none;}

    .nav-container {
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding:10px 0px 30px 0px;
    }

    .logo {
        font-size:22px;
        font-weight:700;
    }

    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([6,4])

    with col1:
        st.markdown('<div class="logo">Jason Sim</div>', unsafe_allow_html=True)

    with col2:
        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.page_link("Home.py", label="Home")

        with c2:
            st.page_link("pages/AboutMe.py", label="About")

        with c3:
            st.page_link("pages/Experiences.py", label="Experiences")

        with c4:
            st.page_link("pages/Projects.py", label="Projects")
