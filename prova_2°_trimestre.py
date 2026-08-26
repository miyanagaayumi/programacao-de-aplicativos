import sqlite3
conexao = sqlite3.connect('rede_bancaria.db')
cursor = conexao.cursor()

def criar_tabelas():
    try:
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
                            REFERENCES conglomerados_financeiros(id)
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
                            INSERT INTO conglomerados_financeiros (nome_banco, codigo_compensacao_bcb) VALUES (?,?)''',
                            (nome_banco, codigo_bcb)
                            )
        cursor.execute(comando_inserir)
        conexao.commit()

        print("conglomerado financeiro cadastrado com sucesso")
    except sqlite3.IntegrityError:
        print("erro: codigo de compensação BCB ja cadastrado")
    except Exception as erro:
        print("erro no cadastro:", erro)
    finally:
        print("encerrando programa...")

def listar_conglomerados():
    try:
        cursor.execute(''' SELECT * FROM conglomerados_financeiros ''')
        conglomerados = cursor.fetchall()

        if not conglomerados:
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
            "UPDATE conglomerados_financeiros SET nome_banco = ?, codigo_compensacao_bcb = ? WHERE id = ?", 
            (nome_banco, codigo_compensacao_bcb, id_conglomerado)
        )
        conexao.commit()
        print("conglomerado atualizado com sucesso")

    except ValueError:
        print("digite um ID valido: ")
    except sqlite3.Error as erro:
        print("erro no banco de dados:", erro)
    except Exception as erro:
        print("erro:", erro)

def deletar_conglomerado():
    try:
        id_conglomerado = int(input("digite o ID do conglomerado que deseja excluir: "))

        cursor.execute(
            ''' DELETE FROM conglomerados_financeiros WHERE id = ?''', (id_conglomerado)            
        )

        conexao.commit()
        print("conglomerado excluido com sucesso")

    except ValueError:
        print("digite um ID valido")
    except sqlite3.Error as erro:
        print("erro no banco de dados:", erro)   

def menu_conglomerados():
     while True:
        try:
            print("\n---- MENU CONGLOMERADO ----")
            print("\n1 - cadastrar")
            print("2 - listar")
            print("3 - atualizar")
            print("4 - excluir")
            print("5 - sair")

            opcao = int(input("escolha uma opção: "))

            if opcao == 1:
                cadastrar_conglomerados()
            elif opcao == 2:
                listar_conglomerados()
            elif opcao == 3:
                atualizar_conglomerado()
            elif opcao == 4:
                deletar_conglomerado()
            elif opcao == 5:
                break
            else:
                print("opção invalida")

        except ValueError:
            print("digite apenas numeros")
        except sqlite3.Error as erro:
            print("erro no banco de dados:", erro)
menu_conglomerados()



def cadastrar_agencias():
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        numero_agencia = input("digite o numero da agencia: ")
        id_conglomerado = int(input("digite o ID do conglomerado: "))

        cursor.execute(
            ''' SELECT id FROM  conglomerados_financeiros WHERE id = ?''',
            (id_conglomerado,)
        )

        if cursor.fetchone() is None:
            print("conglomerado não encontrado")
            return
        
        cursor.execute(
            '''INSERT INTO agencias_bancarias (numero_agencia, id_conglomerado) VALUES (?, ?)''',
            (numero_agencia, id_conglomerado)

        )
        conexao.commit()
        print("agencia cadastrada com sucesso")

    except ValueError:
        print("o id do conglomerado deve ser um numero")
    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)

def listar_agencias():
    try:
        cursor.execute(''' SELECT * FROM agencias_bancarias ''')
        agencias = cursor.fetchall()

        if len(agencias) == 0:
            print("nenhuma agencia cadastrada")
            return

        for agencia in agencias:
            print("id:", agencia[0])
            print("numero da agencia:", agencia[1])
            print("id do conglomerado:", agencia[2])
            print( "-" * 30)
    except sqlite3.Error as erro:
        print("erro no banco de dados:", erro)

def atualizar_agencias():
    try:
        id_agencia = int(input("digite o ID da agencia: "))
        numero_agencia = input("digite o novo numero da agencia: ")
        id_conglomerado = int(input("digite o novo id do conglomerado: "))

        cursor.execute(
            '''SELECT id FROM conglomerados_financeiros WHERE id = ?''',
            (id_conglomerado,)
       )

        if cursor.fetchone() is None:
            print("conglomerado não encontrado")
            return

        cursor.execute(
            ''' UPDATE agencias_bancarias
            SET numero_agencia = ?, id_conglomerado = ? WHERE id = ? ''',
            (numero_agencia, id_conglomerado, id_agencia)
        )

        conexao.commit()
        print("agencia atualizada com sucesso")

    except ValueError:
        print("digite valores validos")
    except sqlite3.Error as erro:
        print("erro no banco de dados:", erro)


def excluir_agencias():
    try:
        id_agencia = int(input("digite o id da agencia que deseja excluir: "))

        cursor.execute(
            '''DELETE FROM agencias_bancarias WHERE id = ?''', 
            (id_agencia,)
        )

        conexao.commit()
        print("agencia excluida com sucesso")

    except ValueError:
        print("digite um id valido")
    except sqlite3.Error as erro:
        print("erro no banco de dados:", erro)


def menu_agencias():
     while True:
        try:
            print("\n---- MENU AGENCIAS ----")
            print("\n1 - cadastrar")
            print("2 - listar")
            print("3 - atualizar")
            print("4 - excluir")
            print("5 - sair")

            opcao = int(input("escolha uma opção: "))

            if opcao == 1:
                cadastrar_agencias()
            elif opcao == 2:
                listar_agencias()
            elif opcao == 3:
                atualizar_agencias()
            elif opcao == 4:
                excluir_agencias()
            elif opcao == 5:
                break
            else:
                print("opção invalida")

        except ValueError:
            print("digite apenas numeros")
        except sqlite3.Error as erro:
            print("erro no banco de dados:", erro)
menu_agencias()
conexao.commit()
conexao.close()