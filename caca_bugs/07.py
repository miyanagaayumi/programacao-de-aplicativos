import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    # 1. Abre a conexão e cria o cursor dentro da função
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    
    # 2. Ativa o suporte a chaves estrangeiras (correção de 'foreing' para 'foreign')
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # 3. Insere os dados na tabela
    cursor.execute(
        "INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)", 
        (nome, id_serie, id_prof)
    )
    
    # 4. Salva as alterações e fecha a conexão
    conexao.commit()
    conexao.close()