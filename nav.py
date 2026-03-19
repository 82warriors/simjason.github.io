import streamlit as st

def navbar():

    st.markdown("""
    <style>
    .nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 0px;
        margin-bottom: 20px;
    }

    .nav-left {
        font-size: 20px;
        font-weight: 600;
    }

    .nav-right a {
        margin-left: 25px;
        text-decoration: none;
        font-weight: 500;
        color: #374151;
    }

    .nav-right a:hover {
        color: #6366F1;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nav">
        <div class="nav-left">🚀 Jason Sim</div>
        <div class="nav-right">
            <a href="/">Home</a>
            <a href="/About">About</a>
            <a href="/Experience">Experience</a>
            <a href="/Projects">Projects</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
