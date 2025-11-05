import  sqlite3

def criar_conexao():
    conexao = sqlite3.connect('hqs.db')
    return conexao

def criar_tabela():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        """ 
            CREATE TABLE IF NOT EXISTS anime (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                ano INTEGER,
                nota DECIMAL(2,2)
            );
        """
    )
    conexao.commit()
    conexao.close()

def inserir_anime(titulo, ano, nota):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        """
            INSERT INTO anime (titulo,ano,nota)
            VALUES (?, ?, ?);
        """,
        (titulo, ano, nota)
    )
    conexao.commit()
    conexao.close()
    print("Anime inserido com sucesso!")

def atualizar_anime(id, titulo, ano, nota):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        """
            UPDATE anime
            SET titulo = ?, ano = ?, nota = ?
            WHERE id = ?;
        """,
        (titulo, ano, nota, id)
    )
    conexao.commit()
    conexao.close()

def excluir_anime(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        """
            DELETE FROM anime
            WHERE id = ?;
        """,
        (id,)
    )
    conexao.commit()
    conexao.close()

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