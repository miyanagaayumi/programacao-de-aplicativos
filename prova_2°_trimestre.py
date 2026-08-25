import sqlite3
conexao = sqlite3.connect('rede_bancaria.db')
cursor = conexao.cursor()

def criar_tabelas():
    try:
        conexao = sqlite3.connect('rede_bancaria.db')
        cursor = conexao.cursor()
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS conglomerados_financeiros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_banco TEXT NOT NULL,
                        codigo_compensacao_bcb INTEGER UNIQUE NOT NULL 
                        )''')

        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS agencias_bancarias (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        numero_agencia TEXT NOT NULL,
                        id_conglomerado INTEGER NOT NULL,
                        FOREIGN KEY (id_conglomerado)
                            REFERENCES conclomerados_financeiros(id)
                            )''')
        conexao.commit()
    except Exception as erro:
        print("Erro ao criar tabela:", erro)
criar_tabelas()
print("banco criado com sucesso")


def cadastrar_conglomerados():
    try:
        nome_banco = input("digite o nome do banco: ")
        codigo_bcb = int(input("digite o seu codigo de compensação: "))

        comando_inserir = (f''' 
                            INSERT INTO conglomerados_financeiros (nome_banco, codigo_compensacao_bcb) VALUES (?,?)
                            ''')
        cursor.execute(comando_inserir)
        conexao.commit()

        print("conglomerado financeiro cadastrado com sucesso")
    except sqlite3.IntegrityError:
        print("erro: codigo de compensação BCB ja cadastrado")
    except Exception as erro:
        print("erro no cadastro:", erro)

def listar_conglomerados():
    try:
        cursor.execute(''' SELECT * FROM conglomerados_financeiros ''')
        conglomerados = cursor.fetchall()

        if not conglomeraods:
            print("nenhum conglomerado cadastrado")
        else:
            for conglomerado in conglomerados:
                print("ID:", conglomerado[0])
                print("nome do banco:", conglomerado[1])
                print("codigo de compensação BCB:", conglomerado[2])
                print("-" * 30)

        conexao.commit()
    except Exception as erro:
        print("erro ao listar conglomerados:", erro)


def atualizar_conglomerado():
    try:
        id_conglomerado = int(input("digite o ID do conglomerado: "))
        nome_banco = input("digite o novo nome do banco: ")
        codigo_bcb = input("digite o novo codigo de compensação BCB: ")

        cursor.execute(
            "UPDATE conglomerados_financeiros SET nome_banco = ?, codigo_compensação_bcb = ? WHERE id = ?", 
            (nome_banco, codigo_compensacao_bcb, id_conglomerado)
        )
            print("conglomerado atualizado com sucesso")
        conexao.commit()
    except ValueError:
        print("digite um ID valido: ")
    except sqlite3.Error as erro:
        print("erro no banco de dados:", erro)
    except Exception as erro:
        print("erro:", erro)

def deletar_conglomerado():
    try:
        