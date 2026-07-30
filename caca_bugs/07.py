import sqlite3

# def cadastrar_turma(nome, id_serie, id_prof):
#     # 1. Abre a conexão e cria o cursor dentro da função
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()
    
#     # 2. Ativa o suporte a chaves estrangeiras (correção de 'foreing' para 'foreign')
#     cursor.execute("PRAGMA foreign_keys = ON;")
    
#     # 3. Insere os dados na tabela
#     cursor.execute(
#         "INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)", 
#         (nome, id_serie, id_prof)
#     )
    
#     # 4. Salva as alterações e fecha a conexão
#     conexao.commit()
#     conexao.close()

#     CORRETO

def criar_tabela_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            id_serie INTEGER,
            id_prof INTEGER,
            FOREIGN KEY (id_serie) REFERENCES series(id),
            FOREIGN KEY (id_prof) REFERENCES professores(id)
        )
    ''')

    conexao.commit()
    conexao.close()

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    try:
        cursor.execute('''
            INSERT INTO turmas (nome, id_serie, id_prof)
            VALUES (?, ?, ?)
        ''', (nome, id_serie, id_prof))

        conexao.commit()
        print("Turma cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: professor ou série não existe.")

    finally:
        conexao.close()

criar_tabela_turmas()
cadastrar_turma("turma A", 1,1)
