import sqlite3
from banco import conectar


def cadastrar_escola(nome, cidade):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            'INSERT INTO escolas (nome, cidade) VALUES (?, ?)',
            (nome, cidade)
        )

        conexao.commit()
        conexao.close()

        print("Escola cadastrada com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar escola: {erro}")


def listar_escolas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()

        conexao.close()

        print("\n--- ESCOLAS ---")

        if not escolas:
            print("Nenhuma escola cadastrada.")
        else:
            for escola in escolas:
                print(
                    f"ID: {escola[0]} | "
                    f"Nome: {escola[1]} | "
                    f"Cidade: {escola[2]}"
                )

    except sqlite3.Error as erro:
        print(f"Erro ao listar escolas: {erro}")


def alterar_escola(id_escola, nome, cidade):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            '''
            UPDATE escolas
            SET nome = ?, cidade = ?
            WHERE id = ?
            ''',
            (nome, cidade, id_escola)
        )

        if cursor.rowcount == 0:
            print("Escola não encontrada.")
        else:
            conexao.commit()
            print("Escola alterada com sucesso!")

        conexao.close()

    except sqlite3.Error as erro:
        print(f"Erro ao alterar escola: {erro}")


def excluir_escola(id_escola):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            'DELETE FROM escolas WHERE id = ?',
            (id_escola,)
        )

        if cursor.rowcount == 0:
            print("Escola não encontrada.")
        else:
            conexao.commit()
            print("Escola excluída com sucesso!")

        conexao.close()

    except sqlite3.IntegrityError:
        print(
            "Não é possível excluir esta escola, pois existem "
            "turmas vinculadas a ela."
        )

    except sqlite3.Error as erro:
        print(f"Erro ao excluir escola: {erro}")

