#Chama a biblioteca que conecta o Banco de Dados(MySQL) com o Python
import sqlite3
#cria um cursor que vai escrever os scripts no MySQL e cria o Banco de Dados
def criar_conexao():
    conexao = sqlite3.connect('Banco_DE_DADOS.db')
    return conexao
#cria a tabela de animes onde vai conter o nome,estudio, data de lançamento,
# data de finalização e avaliação
def criar_tabela():
    conexao = criar_conexao()
    cursor = conexao.cursor()
   
    # Cria tabela principal de animes
    cursor.execute(
        """ 
            CREATE TABLE IF NOT EXISTS anime (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                ano_inicial INTEGER NOT NULL,
                ano_final INTEGER,
                nota REAL
            );
        """
    )
    
    # Cria tabela de avaliações separada
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS avaliacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                anime_id INTEGER NOT NULL,
                nota REAL NOT NULL,
                FOREIGN KEY(anime_id) REFERENCES anime(id)
            );
        """
    )

    conexao.commit()
    conexao.close()
    print("Tabelas 'anime' e 'avaliacao' criadas com sucesso!")
#inserir um novo anime na tabela animes do Banco de dados
def inserir_anime(titulo, ano_inicial, ano_final, nota):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        """
            INSERT INTO anime (titulo,ano_inicial,ano_final,nota)
            VALUES (?, ?, ?, ?);
        """,
        (titulo, ano_inicial, ano_final, nota)
    )
    conexao.commit()
    conexao.close()
    print("Anime inserido com sucesso!")
#atualiza a tabela animes com novas informaçoes(se necessario)
def atualizar_anime(id, titulo, ano_inicial,ano_final, nota):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        """
            UPDATE anime
            SET titulo = ?, ano_inicial = ?,ano_final = ?, nota = ?
            WHERE id = ?;
        """,
        (titulo, ano_inicial,ano_final, nota, id)
    )
    conexao.commit()
    conexao.close()
#adiciona uma nova avaliação á um anime que ja existe e altera a nota para a 
#media das avaliações adicionadas
def adicionar_avaliacao(anime_id, nota):
    
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO avaliacao (anime_id, nota) VALUES (?, ?);",
        (anime_id, nota)
    )

    cursor.execute(
        "SELECT AVG(nota) FROM avaliacao WHERE anime_id = ?;",
        (anime_id,)
    )
    media = cursor.fetchone()[0]

    cursor.execute(
        "UPDATE anime SET nota = ? WHERE id = ?;",
        (media, anime_id)
    )

    conexao.commit()
    conexao.close()

    print(f"⭐ Avaliação adicionada! Nova média: {round(media, 2)}")
#lista a tabela animes com as informações dos animes
def listar_animes():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        """
            SELECT * FROM anime;
        """
    )
    animes = cursor.fetchall()
    conexao.close()
    return animes
#cria uma tabela de usuarios no banco de dados
def criar_tabela_user():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS usuario (
                id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                pasword TEXT NOT NULL
            );"""
    )

    conexao.commit()
    conexao.close()
    print('As tabelas Usuarios foram criadas')

#lista a tabela de usuarios
def listar_tabela_user():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute(
        """
            SELECT * FROM usuario;

            """
    )

    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

# cadastra um novo usuario no banco de dados
def inserir_user(username, pasword):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute(
        """ INSERT INTO usuario (username, pasword)
        VALUES (?,?);"""
        (username, pasword)
    )

    conexao.commit()
    conexao.close()
    print('Usuario cadastrado com sucesso')