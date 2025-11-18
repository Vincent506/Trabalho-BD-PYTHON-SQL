import streamlit as st
from datb_anime import datab

st.set_page_config('Cadastro', "🔐", "centered")

def salvar_usuario(nome_user,senha_user):
    datab.inserir_user(nome_user,senha_user)
    st.success(f'Novo usuario salvo com sucesso!', icon="✅")

st.title('CADASTRO DE NOVO USUÁRIO 🔐')

with st.form(key='formulario de cadastro'):
    testenome = st.text_input('Crie o seu nome do Usuario')
    testesenha = st.text_input('Crie sua senha')
    submition = st.form_submit_button('cadastrar')

    if submition:
        if testenome and testesenha:
            salvar_usuario(testenome,testesenha)
            st.info('usuario cadastrado com sucesso', icon="ℹ️")
        else:
            st.warning('Preencha todos os campos por favor',  icon="⚠️")