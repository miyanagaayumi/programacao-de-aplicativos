import sqlite3
conexao = sqlite3.connect('gestao_escolar.bd')
conexao.execute("PRAGMA foreign_keys = ON;")

return conexao

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS escola (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade TEXT NOT NULL
            )
            ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS turma (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                ano INTEGER NOT NULL,
                escola_id INTEGER NOT NULL,
                FOREIGN KEY (escola_id)
                    REFERENCES escola(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                turma_id INTEGER NOT NULL,
                FORENIGN KEY (turma_id)
                    REFERENCES turma(id)
            )
        ''')
        conexao.commit()
    
    except sqlite3.Error as erro:
        print(f"erro ao criar as tabelas: {erro}")
    finally:
        conexao.close()