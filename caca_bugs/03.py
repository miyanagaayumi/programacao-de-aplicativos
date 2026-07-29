import sqlite3

# def criar_tabelas():
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     #este bloco quebra ao rodar pela primeira vez em um banco limpo. pq?
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS series (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome_serie text, 
#             ID_ESCOLA integer,
#             FOREIGN KEY (id_escola) REFERENCES escolas(id)
#         )
#         ''')
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS escolas (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome TEXT
#         )
#     ''')
#     conexao.commit()
#     conexao.close()
    

#CORRETO 


def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_serie TEXT NOT NULL,
                id_escola INTERGER,
                FOREIGN KEY (id_escola) REFERENCES escolas (id)
            )
        ''')

    conexao.commit()
    conexao.close()
    print("tabela criada com sucesso")

criar_tabelas()

