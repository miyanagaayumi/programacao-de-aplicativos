import sqlite3
conexao = None
conexao = sqlite3.connect('gestao_escolar.db')
cursor = conexao.cursor()


def cadastrar_escolas():
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        cursor = conexao.cursor()
        nome_escola = input("Insira o nome da escola: ")
        cidade_esc = input("Informe o nome da cidade: ")
        comando_inserir = "INSERT INTO escolas (nome, cidade) VALUES (?, ?)"

        cursor.execute(comando_inserir, (nome_escola, cidade_esc))
        conexao.commit()
        print("Cadastro concluido!")

    except ValueError as e:
        print("Digite apenas nomes! ", e)
    except sqlite3.IntegrityError as e:
        print("Erro! Informações já cadastradas! ", e)
    finally:
        if conexao:
            conexao.commit() 
            conexao.close()


def listar_escolas():
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM escolas")

        info_escolas = cursor.fetchall()

        print(">>> ESCOLAS CADASTRADASTRADAS <<<")

        if not info_escolas:
            print("Nenhuma informação encontrada!")

        else:
            for inf in info_escolas:
                print(f"ID: {inf[0]}")
                print(f"Nome: {inf[1]}")
                print(f"Cidade: {inf[2]}")


    except sqlite3.Error as e:
        print("Erro do sqlite: ", e)


def atualizar_escolas():
    conexao = sqlite3.connect('gestao_escolar.db')
    cursor = conexao.cursor()
    listar_escolas()

    try:
        id_escola = int(input("Insira o id da escola que deseja alterar: "))
        nova_escola = input("Informe o nome novo: ")
        cursor.execute("UPDATE escolas SET nova_escola = ? WHERE id = ?", (nova_escola))

        conexao.commit()
        print("Nome atualizado com sucesso!")

    except sqlite3.Error as e:
        print("Não foi possivel atualizar!", e)


def excluir_escolas():
    conexao = sqlite3.connect('gestao_escolar.db')
    cursor = conexao.cursor()
    listar_escolas()

    try:
        id_escolas = int(input("Informe o id da escola que deseja excluir: "))
        cursor.execute("DELETE FROM escolas WHERE id = ?", (id_escolas,))


        conexao.commit()
        print("Escola deletada com sucesso!")

    except sqlite3.Error as e:
            print("Erro: Escola não deletada.", e)