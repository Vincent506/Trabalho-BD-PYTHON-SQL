import streamlit as st
from datb_anime import datab
from datetime import date


datab.criar_tabela()

def salvar_anime(titulo, ano, nota):
    datab.inserir_anime(titulo,ano,nota)