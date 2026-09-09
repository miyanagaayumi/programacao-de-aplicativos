import sqlite3
from banco import conectar


def cadastrar_turma(nome_turma, id_escola):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            '''
            INSERT INTO turmas (nome_turma, id_escola)
            VALUES (?, ?)
            ''',
            (nome_turma, id_escola)
        )

        conexao.commit()
        conexao.close()

        print("Turma cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: a escola informada não existe.")

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar turma: {erro}")


def listar_turmas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM turmas")
        turmas = cursor.fetchall()

        conexao.close()

        print("\n--- TURMAS ---")

        if not turmas:
            print("Nenhuma turma cadastrada.")
        else:
            for turma in turmas:
                print(
                    f"ID: {turma[0]} | "
                    f"Nome: {turma[1]} | "
                    f"ID Escola: {turma[2]}"
                )

    except sqlite3.Error as erro:
        print(f"Erro ao listar turmas: {erro}")


def alterar_turma(id_turma, nome_turma, id_escola):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            '''
            UPDATE turmas
            SET nome_turma = ?, id_escola = ?
            WHERE id = ?
            ''',
            (nome_turma, id_escola, id_turma)
        )

        if cursor.rowcount == 0:
            print("Turma não encontrada.")
        else:
            conexao.commit()
            print("Turma alterada com sucesso!")

        conexao.close()

    except sqlite3.IntegrityError:
        print("Erro: a escola informada não existe.")

    except sqlite3.Error as erro:
        print(f"Erro ao alterar turma: {erro}")


def excluir_turma(id_turma):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM turmas WHERE id = ?",
            (id_turma,)
        )

        if cursor.rowcount == 0:
            print("Turma não encontrada.")
        else:
            conexao.commit()
            print("Turma excluída com sucesso!")

        conexao.close()

    except sqlite3.IntegrityError:
        print(
            "Não é possível excluir esta turma, pois existem "
            "alunos vinculados a ela."
        )

    except sqlite3.Error as erro:
        print(f"Erro ao excluir turma: {erro}")
