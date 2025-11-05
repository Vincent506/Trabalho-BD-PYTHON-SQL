import sqlite3

#1 - Conectando no BD
conexao = sqlite3.connect('animes.db')
cursor = conexao.cursor()

#2 - Inserindo dados
cursor.execute(
    """
        INSERT INTO  anime(nome, ano, nota)
        VALUES ('Naruto', 2002, 8.3)
        
    """
)
conexao.commit()
conexao.close()
print("Dados inseridos na tabela")