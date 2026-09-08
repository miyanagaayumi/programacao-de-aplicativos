import sqlite3
from banco import conectar


def cadastrar_aluno(nome, idade, id_turma):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            '''
            INSERT INTO alunos (nome, idade, id_turma)
            VALUES (?, ?, ?)
            ''',
            (nome, idade, id_turma)
        )

        conexao.commit()
        conexao.close()

        print("Aluno cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: a turma informada não existe.")

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar aluno: {erro}")


def listar_alunos():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()

        conexao.close()

        print("\n--- ALUNOS ---")

        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in alunos:
                print(
                    f"ID: {aluno[0]} | "
                    f"Nome: {aluno[1]} | "
                    f"Idade: {aluno[2]} | "
                    f"ID Turma: {aluno[3]}"
                )

    except sqlite3.Error as erro:
        print(f"Erro ao listar alunos: {erro}")


