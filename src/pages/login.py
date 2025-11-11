import streamlit as st
from datb_anime import datab


teste = datab.listar_tabela_user()

if not teste:
    datab.criar_tabela_user()

st.set_page_config(page_title='Login', page_icon='🔒', layout='centered')


st.title('🔒 Avaliador de Animes Login')

st.write('Por favor, insira suas credenciais para continuar.')

username = st.text_input('Usuario ou email')
pasword = st.text_input('Senha', type='password')

if st.button('Entrar'):
    if datab.checar_usuario(username,pasword) == True:
        st.page_link('pages/application.py', label= 'Home', icon="🏠")
    else:
        st.write('usuario não encontrado')

if st.button('Cadastrar'):
    st.page_link('pages/cadastro.py', label= 'Abrir Cadastro', icon="📃")

