import sqlite3
def cadastrar_lista_alunos():
    lista = [("ana", 1), ("carlos", 1), ("beatriz", 2)]
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    #O comando executemany quebra com a mensagem: Function takes exactly 2 arguments.
    # Como passar a lista de dados da forma correta dele?
    cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", lista)

    conexao.commit()
    conexao.close()