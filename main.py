import streamlit as st

pages = [
    st.Page("pages/login.py", title="login"),
    st.Page("pages/home.py", title="Home")
]

nav = st.navigation(pages)


if nav.title != "login" and st.button("Sair"):
    st.session_state.clear()
    st.switch_page("pages/login")

nav.run()