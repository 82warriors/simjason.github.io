import streamlit as st

def navbar():

    st.markdown("""
    <style>

    .nav-container {
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding:10px 0;
        margin-bottom:20px;
    }

    .logo {
        font-size:20px;
        font-weight:700;
        color:#6366F1;
    }

    .nav-links a {
        margin-left:25px;
        text-decoration:none;
        font-weight:500;
        color:#374151;
        transition:0.2s;
    }

    .nav-links a:hover {
        color:#6366F1;
    }

    .active {
        color:#6366F1 !important;
        font-weight:600;
    }

    </style>
    """, unsafe_allow_html=True)

    # Get current page
    page = st.session_state.get("page", "Home")

    # Navbar HTML
    st.markdown(f"""
    <div class="nav-container">
        <div class="logo">Jason Sim</div>

        <div class="nav-links">
            <a href="/" class="{ 'active' if page=='Home' else '' }">Home</a>
            <a href="/AboutMe" class="{ 'active' if page=='About' else '' }">About</a>
            <a href="/Projects" class="{ 'active' if page=='Projects' else '' }">Projects</a>
            <a href="/Experiences" class="{ 'active' if page=='Experience' else '' }">Experience</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
