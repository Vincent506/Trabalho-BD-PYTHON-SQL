import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('animes.db')
cursor = conexao.cursor()

# 2 - Leitura de dados
dados = cursor.execute("SELECT * FROM anime")

print(dados.fetchall())