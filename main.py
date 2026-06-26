import streamlit as st

#Páginas para navegação
pages = [
    st.Page("pages/login.py", title="login"),
    st.Page("pages/home.py", title="Home")
]

#Cria variável de renderização
nav = st.navigation(pages)

#lógica do botão sair
if nav.title != "login" and st.button("Sair"):
    st.session_state.clear()
    st.switch_page("pages/login.py")

nav.run()