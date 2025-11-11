import streamlit as st

st.set_page_config(page_title="Anime BD", page_icon="🎬")

st.title("🎬 Banco de Animes")
st.write("Bem-vindo! Sinta-se á vontade para avaliar ou adicionar seus animes favoritos!!")

st.page_link("pages/login.py", label="🔑 Login")
st.page_link("pages/cadastro.py", label="📃 Cadastro")