import streamlit as st

def navbar():

    if "page" not in st.session_state:
        st.session_state.page = "home"

    def set_page(page):
        st.session_state.page = page

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

    .nav-right button {
        margin-left: 15px;
        background: none;
        border: none;
        font-weight: 500;
        color: #374151;
        cursor: pointer;
        font-size: 16px;
    }

    .nav-right button:hover {
        color: #6366F1;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 5])

    with col1:
        st.markdown("🚀 **Jason Sim**")

    with col2:
        cols = st.columns(4)
        with cols[0]:
            if st.button("Home"):
                set_page("home")
        with cols[1]:
            if st.button("About"):
                set_page("about")
        with cols[2]:
            if st.button("Experience"):
                set_page("experience")
        with cols[3]:
            if st.button("Projects"):
                set_page("projects")
