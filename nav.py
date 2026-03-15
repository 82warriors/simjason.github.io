import streamlit as st

def navbar():

    st.markdown("""
    <style>

    [data-testid="stSidebar"] {display:none}

    .nav-container{
        display:flex;
        justify-content:flex-end;
        gap:40px;
        padding-top:20px;
        padding-bottom:20px;
        font-size:18px;
        font-weight:500;
    }

    .nav-link{
        text-decoration:none;
        color:#111;
    }

    .nav-link:hover{
        color:#4cc9f0;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nav-container">

    <a class="nav-link" href="/">Home</a>
    <a class="nav-link" href="/AboutMe">About</a>
    <a class="nav-link" href="/Experiences">Experiences</a>
    <a class="nav-link" href="/Projects">Projects</a>

    </div>
    """, unsafe_allow_html=True)
