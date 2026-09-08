import sqlite3
from banco import conectar


def cadastrar_escola(nome, cidade):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO escolas (nome, cidade) VALUES (?, ?)",
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

