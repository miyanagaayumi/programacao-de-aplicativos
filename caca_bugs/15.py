import sqlite3
def criar_tabela_turma():
    conexao = sqlite.connect('sistema_escola.db')
    cursor = conexao.cursor()
    # o SQLite acusa erro de sintaxe próximo ao FOREING KEY. cade o erro?
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomr_turma TEXT, 
            id_serie,
            FOREIGN KEY (id_serie) REFERENCES serie(id)
        )
    ''')
    conexao.commmit()
    conexao.close()
    