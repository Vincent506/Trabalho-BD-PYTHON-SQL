import streamlit as st
from datb_anime import datab
from datetime import date


teste = datab.listar_animes()

if not teste:
    datab.criar_tabela()


def salvar_anime(titulo, ano_inicial,ano_final, nota):
    datab.inserir_anime(titulo,ano_inicial,ano_final,nota)
    st.success(f'Anime "{titulo}" salvo com sucesso!', icon="✅")

def carregar_animes():
    try:
        dados = datab.listar_animes()
        if not dados:
            st.info('Nenhum anime encontrado no Banco de Dados',  icon="ℹ️")
            return []
        
        animes_dados = [
            {
                "id": anim[0],
                "titulo": anim[1],
                "ano_inicial": anim[2],
                "ano_final":anim[3],
                "nota": anim[4]
            }
                for anim in dados
        ]
        return animes_dados
    except Exception as e:
        st.error(f'Erro ao carregar os Animes: {e}')
        return []
    

st.set_page_config(page_title="Avaliador de Animes", layout="wide")
st.title("Avaliador de Animes")
st.subheader("Bem-vindo ao Avaliador de Animes!")

aba1, aba2, aba3 = st.tabs(['Novo Anime', 'Avaliar Anime', 'Vizualizar Avaliações'])

with aba1:
    opcoes = [1, 2, 3, 4, 5]

    st.header('Adicionar novo Anime')

    with st.form(key="Form Avaliação"):
        titulo = st.text_input('Título', placeholder='Digite o nome no Anime')
        ano_lanc = st.date_input('Ano de lançamento', max_value=date.today(), min_value=date(1900, 1, 1))
        ano_fim = st.date_input('Ano de termino(se ouver)', max_value=date.today(), min_value=date(1900, 1, 1))
        nota = st.select_slider("Escolha sua avaliação inicial:",options=opcoes,)
        submittion = st.form_submit_button(label="Adicionar Novo Anime", icon="🔥")

        if submittion:
            if titulo and ano_lanc and nota:
                salvar_anime(titulo,ano_lanc,ano_fim,nota)
                st.info('Adição feita com sucesso!',icon="ℹ️")
            else:
                st.warning('Preencha todos os campos por favor',  icon="⚠️")



with aba2:
    st.header("Avaliar um Anime")

    animes_dados = carregar_animes()
    if not animes_dados:
        st.info("Nenhum Anime disponível para avaliação.", icon="ℹ️")
    else:
        opcoes = {f'{anim["id"]} - {anim["titulo"]}': anim for anim in animes_dados}
        escolha = st.selectbox("Selecione um anime para avaliar:", list(opcoes.keys()))

        anime_select = opcoes[escolha]
        
        

        with st.form("edita_animes"):
            st.write(f'Ano de Lançamento: {anime_select['ano_inicial']}')
            st.write(f'Ano final: {anime_select['ano_final']}')
            
            nova_nota= st.number_input("Nota", value=anime_select['nota'])
            
            atualizar_submitted = st.form_submit_button("Adicionar Nova Avaliação")
            if atualizar_submitted:
                index = int(anime_select['id'])
                datab.adicionar_avaliacao(index,nova_nota)
                st.success(f'Anime "{anime_select['titulo']}" avaliado com sucesso!', icon="✅")

            


with aba3:
    st.header("Visualizar animes com notas")

    st.subheader("📖 Lista de Animes")
    if st.button("🔄 Recarregar Animes"):
        anime_data = datab.listar_animes()
        if anime_data:
            st.table(anime_data)
        else:
            st.warning('Não temos animes no Banco de Dados',  icon="⚠️")
