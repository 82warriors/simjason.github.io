import streamlit as st

def navbar():

    st.markdown("""
    <style>

    /* hide sidebar */
    [data-testid="stSidebar"] {display:none;}

    /* navigation bar */
    .nav-container{
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding:20px 60px;
        border-bottom:1px solid #eee;
        font-family:sans-serif;
    }

    /* logo */
    .nav-logo{
        font-size:20px;
        font-weight:700;
    }

    /* menu */
    .nav-menu{
        display:flex;
        gap:40px;
        font-size:16px;
    }

    .nav-link{
        text-decoration:none;
        color:#111;
        font-weight:500;
        position:relative;
    }

    /* underline animation */
    .nav-link::after{
        content:"";
        position:absolute;
        width:0;
        height:2px;
        left:0;
        bottom:-4px;
        background:#6366f1;
        transition:width 0.25s ease;
    }

    .nav-link:hover::after{
        width:100%;
    }

    .nav-link:hover{
        color:#6366f1;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nav-container">

        <div class="nav-logo">
        Jason Sim
        </div>

        <div class="nav-menu">
            <a class="nav-link" href="/">Home</a>
            <a class="nav-link" href="/AboutMe">About</a>
            <a class="nav-link" href="/Experiences">Experiences</a>
            <a class="nav-link" href="/Projects">Projects</a>
        </div>

    </div>
    """, unsafe_allow_html=True)
