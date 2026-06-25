# Importando bibliotecas
import streamlit as st
import utils.functions as f
import controllers.login_controller as login_controller

st.set_page_config(initial_sidebar_state="collapsed")

# Acesso de login
with st.form('login'):
    st.space('small')
    col1, col2, col3 = st.columns([3,1,3])
    with col2:
        st.image('https://www.ifmg.edu.br/santaluzia/logo-1.png/@@images/e5a4798c-b061-4a43-9d97-154f96b36290.png', use_container_width=True)
    st.space('xxsmall')

    st.title("Login")
    st.caption('Entre com suas credenciais')
    st.space('xxsmall')
    user = st.text_input('**ID**')
    password = st.text_input('**Senha**')

    btn_button = st.form_submit_button('Entrar', use_container_width=True, type='primary', icon=':material/mail:')
    st.space('small')

    if btn_button:
        if login_controller.login_validation(user, password):
            st.switch_page("pages/home.py")
