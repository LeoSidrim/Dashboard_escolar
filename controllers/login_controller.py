import streamlit as st
users = {
    "leonardo" : "12345",
    "gael" : "12345"
}
# Decorator 
# Altera o comportamento da função sem alterar   o corpo dela
def login_validation(username: str, password: str) -> bool:
    # Validação se o cara não deixou em branco qualquer coisa
    if username == '' or password == '':
        st.warning('Preencha todos os campos')
        return False

    # Procura o usuário dentro do dicionário, se ele existir, entra na página.
    for user_item, pass_item in users.items():
        if user_item == username and pass_item == password: 
            return True

    # Caso o usuário não exista, aparece esse aviso
    st.warning("Usuário não cadastrado.\nContate os administradores para ter acesso.")
    return False