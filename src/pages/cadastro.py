import streamlit as st
from datb_anime import datab

st.set_page_config('Cadastro', "🔐", "centered")

def salvar_usuario(nome, senha):
    datab.inserir_user(nome,senha)
    st.success(f'Novo usuario salvo com sucesso!', icon="✅")

