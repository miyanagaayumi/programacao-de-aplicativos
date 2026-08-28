#ALUNOS
import sqlite3

def cadastrar_alunos():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db') 
        cursor = conexao.cursor()  
        cursor.execute(''' 
                        CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        telefone TEXT,
                        turma TEXT,
                        idade INTEGER, 
                        cidade TEXT, 
                        endereco TEXT,
                        estado TEXT,
                        cpf TEXT UNIQUE NOT NULL,
                        professor_id INTEGER
                        )''') 

        nome_aluno = input("nome: ") 
        idade_aluno = int(input("idade: ")) 
        turma_aluno = input("turma: ") 
        telefone_aluno = input("telefone: ")  
        cpf_aluno = input("cpf: ") 
        cidade_aluno = input("cidade: ")
        endereco_aluno = input("endereço: ")
        estado_aluno = input("estado: ")

        comando_inserir = (f'''
                            INSERT INTO alunos (nome, telefone, turma, idade, cpf)
                            VALUES ('{nome_aluno}', '{idade_aluno}', '{turma_aluno}', '{telefone_aluno}', '{cpf_aluno}', '{cidade_aluno}', '{endereco_aluno}', '{estado_aluno}')''') 

        cursor.execute(comando_inserir) 
        conexao.commit() 

    except ValueError:
        print("erro de valor no cadastro tente novamente")
    except TypeError:
        print("erro de tipo de dados") 
    except ZeroDivisionError:
        print("erro de tentativa de dividir")
    except FileNotFoundError:
        print("erro de arquivo nao encontrado")	
    except Exception:
        print("Classe base da maioria dos erros.")	
    finally:
        print("encerrando programa")
        conexao.close() 

def listar_alunos():
    try: 
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()
        cursor.execute(''' SELECT * FROM alunos ''')
        alunos = cursor.fetchall()
        if not alunos:
            print("nenhum aluno cadastrado")
        else:
            for aluno in alunos:
                print(f"ID: {aluno[0]}")
                print(f"Nome: {aluno[1]}")
                print(f"Telefone: {aluno[2]}")
                print(f"Turma: {aluno[3]}")
                print(f"Idade: {aluno[4]}")
                print(f"CPF: {aluno[5]}")
                print(f"cidade: {aluno[6]}")
                print(f"endereco: {aluno[7]}")
                print(f"estado: {aluno[8]}")
                print("-" * 30)
    except ValueError:
        print("erro de valor no cadastro tente novamente")
    except TypeError:
        print("erro de tipo de dados") 
    except ZeroDivisionError:
        print("erro de tentativa de dividir")
    except FileNotFoundError:
        print("erro de arquivo nao encontrado")	
    except Exception:
        print("Classe base da maioria dos erros.")	
    finally:
        print("encerrando programa")                 
        conexao.close()

def alterar_alunos():
    try:
        listar()
        conexao = sqlite3.connect("escola_demonstracao.db")
        cursor = conexao.cursor()

        id_aluno = int(input("digite o id que deseja alterar: "))

        cursor.execute(f'''SELECT * FROM Alunos WHERE id = {id_aluno}''')
        alunos = cursor.fetchone()
        if not id_aluno:
            print("não encontrado!")
        else:
            novo_nome = input("digite o novo nome: ")
            novo_telefone = input("digite o novo telefone: ")
            novo_turma = input("digite a nova turma: ")
            novo_idade = int(input("digite a nova idade: "))
            novo_cpf = input("digite o novo cpf: ")
            print("\ndepois da alteração:")
            print(cursor.fetchone())
            comando = (f'''UPDATE alunos SET nome = '{novo_nome}', telefone = '{novo_telefone}', materia = '{novo_turma}', idade = '{novo_idade}', cpf = '{novo_cpf}''')
        conexao.commit()
    except ValueError:
        print("erro de valor no cadastro tente novamente")
    except TypeError:
        print("erro de tipo de dados") 
    except ZeroDivisionError:
        print("erro de tentativa de dividir")
    except FileNotFoundError:
        print("erro de arquivo nao encontrado")	
    except Exception:
        print("Classe base da maioria dos erros.")	
    finally:
        print("encerrando programa")
        conexao.close()

def deletar_alunos():
    try:
        listar_alunos()
        id_aluno = int(input("Qual ID deseja deletar: "))
        cursor.execute(f'''DELETE FROM alunos WHERE id = {id_aluno}''')
        conexao.commit()
        print("aluno(a) deletado")
    except ValueError:
        print("erro de valor no cadastro tente novamente")
    except TypeError:
        print("erro de tipo de dados") 
    except ZeroDivisionError:
        print("erro de tentativa de dividir")
    except FileNotFoundError:
        print("erro de arquivo nao encontrado")	
    except Exception:
        print("Classe base da maioria dos erros.")	
    finally:
        print("encerrando programa")


def menu():
    try:
        while True:
            print("\n--- TABELA ALUNOS ---")
            print("\n SISTEMA ESCOLAR ")  
            print("1. Cadastrar aluno") 
            print("2. Listar aluno") 
            print("3. Atualizar aluno") 
            print("4. Excluir aluno") 
            print("5. Sair")
                
            opcao = input("Escolha uma opção: ")

            if opcao == '1': cadastrar_alunos()
            elif opcao == '2': listar_alunos() 
            elif opcao == '3': alterar_alunos() 
            elif opcao == '4': deletar_alunos() 
            elif opcao == '5': break
            else: 
                print("Opção inválida!")
    except ValueError:
        print("erro de valor no cadastro tente novamente")
    except TypeError:
        print("erro de tipo de dados") 
    except ZeroDivisionError:
        print("erro de tentativa de dividir")
    except FileNotFoundError:
        print("erro de arquivo nao encontrado")	
    except Exception:
        print("Classe base da maioria dos erros.")	
    finally:
        print("encerrando programa")
menu()


#PROFESSOR
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()


def criar_professor():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS professores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_completo TEXT NOT NULL,
                        telefone TEXT,
                        materia TEXT,
                        idade INTEGER, 
                        cpf TEXT UNIQUE NOT NULL, 
                        salario REAL,
                        nome_da_escola TEXT
                            )
                        ''')

        nome_professor = input("nome: ")
        telefone_professor = input("telefone: ")
        materia_professor = input("materia: ")
        idade_professor = int(input("idade: "))
        cpf_professor = input("cpf: ")
        salario = float(input("salario: "))
        nome_escola = input("nome da escola: ")

        comando_inserir = (f'''
                            INSERT INTO professores (nome_completo, telefone, materia, idade, cpf, salario, nome_da_escola)
                            VALUES ('{nome_professor}', '{telefone_professor}', '{materia_professor}', {idade_professor}, '{cpf_professor}', {salario}, '{nome_escola}')''')

        cursor.execute(comando_inserir)
        conexao.commit()
    except ValueError:
        print("erro de valor no cadastro tente novamente")
    except TypeError:
        print("erro de tipo de dados") 
    except ZeroDivisionError:
        print("erro de tentativa de dividir")
    except FileNotFoundError:
        print("erro de arquivo nao encontrado")	
    except Exception:
        print("Classe base da maioria dos erros.")	
    finally:
        print("encerrando programa")


def listar_professores():
    try: 
        cursor.execute(''' SELECT * FROM professores ''')
        professores = cursor.fetchall()
        if not professores:
            print("nenhum professor cadastrado")
        else:
            for professor in professores:
                print(f"id = {professor[0]}")
                print(f"nome = {professor[1]}")
                print(f"telefone = {professor[2]}")
                print(f"materia = {professor[3]}")
                print(f"idade = {professor[4]}")
                print(f"cpf = {professor[5]}")
                print(f"salario = {professor[6]}")
                print(f"nome da escola = {professor[7]}")

    except ValueError:
        print("erro de valor no cadastro tente novamente")
    except TypeError:
        print("erro de tipo de dados") 
    except ZeroDivisionError:
        print("erro de tentativa de dividir")
    except FileNotFoundError:
        print("erro de arquivo nao encontrado")	
    except Exception:
        print("Classe base da maioria dos erros.")	
    finally:
        print("encerrando programa")

def alterar_professor():
    try:
        id_professor = int(input("digite o id do professor: "))
        cursor.execute(f''' SELECT * FROM professores WHERE id = {id_professor}''')
        professores = cursor.fetchone()
        if not professores: 
            print("proessor não encontrado!")
            return
        else: 
            novo_nome = input("novo nome: ") 
            novo_telefone = input("novo telefone: ") 
            nova_materia = input("nova materia: ")
            nova_idade = int(input("nova idade: "))
            novo_cpf = input("novo cpf: ")
            novo_salario = float(input("novo salario: "))
            nova_escola = input("nova escola: ")

            comando = (f'''UPDATE professores SET nome = '{novo_nome}', telefone = '{novo_telefone}', materia = '{nova_materia}', idade = {nova_idade}, cpf = '{novo_cpf}', salario = {novo_salario}, escola = '{nova_escola}' WHERE id = {id_professor}''')
    except ValueError:
        print("erro de valor no cadastro tente novamente")
    except TypeError:
        print("erro de tipo de dados") 
    except ZeroDivisionError:
        print("erro de tentativa de dividir")
    except FileNotFoundError:
        print("erro de arquivo nao encontrado")	
    except Exception:
        print("Classe base da maioria dos erros.")	
    finally:
        print("encerrando programa")

def deletar_professor(): 
    try:
        listar_professores()
        id_professor = int(input("Qual ID deseja deletar: "))
        cursor.execute(f'''DELETE FROM professores WHERE id = {id_professor}''')
        conexao.commit()
        print("professor deletado")
    except ValueError:
        print("erro de valor no cadastro tente novamente")
    except TypeError:
        print("erro de tipo de dados") 
    except ZeroDivisionError:
        print("erro de tentativa de dividir")
    except FileNotFoundError:
        print("erro de arquivo nao encontrado")	
    except Exception:
        print("Classe base da maioria dos erros.")	
    finally:
        print("encerrando programa")

def menu():
    try:
        while True:
            print("\n--- TABELA PROFESSORES ---")
            print("\n SISTEMA ESCOLAR ")  
            print("1. Cadastrar professor") 
            print("2. Listar professor") 
            print("3. Atualizar professor") 
            print("4. Excluir professor") 
            print("5. Sair")
                
            opcao = input("Escolha uma opção: ")

            if opcao == '1': criar_professor()
            elif opcao == '2': listar_professores() 
            elif opcao == '3': alterar_professor() 
            elif opcao == '4': deletar_professor() 
            elif opcao == '5': break
            else: print("Opção inválida!")
    except ValueError:
        print("erro de valor no cadastro tente novamente")
    except TypeError:
        print("erro de tipo de dados") 
    except ZeroDivisionError:
        print("erro de tentativa de dividir")
    except FileNotFoundError:
        print("erro de arquivo nao encontrado")	
    except Exception:
        print("Classe base da maioria dos erros.")	
    finally:
        print("encerrando programa")
menu()
conexao.close()

