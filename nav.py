import streamlit as st

def navbar():

    st.markdown("""
    <style>

    [data-testid="stSidebar"] {display:none}

    .nav{
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding:20px 60px;
        border-bottom:1px solid #eee;
        font-family:sans-serif;
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

    .menu a{
        text-decoration:none;
        color:#111;
        font-weight:500;
    }

    .menu a:hover{
        color:#6366f1;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nav">

        <div class="logo">
        Jason Sim
        </div>

        <div class="menu">
            <a href="/">Home</a>
            <a href="/AboutMe">About</a>
            <a href="/Experiences">Experiences</a>
            <a href="/Projects">Projects</a>
        </div>

    </div>
    """, unsafe_allow_html=True)
