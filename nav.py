import streamlit as st

def navbar():

    st.markdown("""
    <style>

    [data-testid="stSidebar"] {display:none}

    .nav-container{
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding:20px 40px;
        border-bottom:1px solid #eee;
        font-family: sans-serif;
    }

    .logo{
        font-size:20px;
        font-weight:700;
    }

    .menu{
        display:flex;
        gap:40px;
        font-size:16px;
    }

    .menu-item{
        cursor:pointer;
        color:#111;
        text-decoration:none;
    }

    .menu-item:hover{
        color:#6366f1;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-container">', unsafe_allow_html=True)

    col1, col2 = st.columns([6,4])

    with col1:
        st.markdown('<div class="logo">Jason Sim</div>', unsafe_allow_html=True)

    with col2:

        colA, colB, colC, colD = st.columns(4)

        with colA:
            if st.button("Home"):
                st.switch_page("Home.py")

        with colB:
            if st.button("About"):
                st.switch_page("pages/AboutMe.py")

        with colC:
            if st.button("Experiences"):
                st.switch_page("pages/Experiences.py")

        with colD:
            if st.button("Projects"):
                st.switch_page("pages/Projects.py")

    st.markdown('</div>', unsafe_allow_html=True)
