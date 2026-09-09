import sqlite3

nome_banco = 'gestao_escolar.db'

def conectar():
    conexao = sqlite3.connect(nome_banco)
    conexao.execute('PRAGMA foreign_keys = ON;')
    return conexao

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        )
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS turmas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cidade TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        id_turma INTEGER NOT NULL,
        FOREIGN KEY (id_turma) REFERENCES turmas (id)
    )
''')

conexao.commit()
conexao.close()