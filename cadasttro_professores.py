import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()


def criar_professor():
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS professores (
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
    telefone_professor = input("idade: ")
    materia_professor = input("materia: ")
    idade_professor = int(input("idade: "))
    cpf_professor = input("cpf: ")
    salario = float(input("salario: "))
    nome_escola = input("nome da escola: ")

    comando_inserir = (f'''
                        INSERT INTO professores (nome, telefone, materia, idade, cpf, salario, nome da escola)
                        VALUES ('{nome_professor}', '{telefone_professor}', '{materia_professor}', {idade_professor}, '{cpf_professor}', {salario}, '{nome_escola}')''')

    cursor.execute(comando_inserir)
    conexao.commit()
    

def listar_professores():
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
            print(f"nome da escola = {proessor[7]}")


def alterar_professor():
    id_professor = int(input("digite o id do professor: "))
    cursor.execute(''' SELECT nome, telefone, marteria, idade, CPF, salario, nome da escola FROM professores WHERE id = {id_professor}''')
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

        comando = (f'''UPDATE professores SET nome = '{novo_nome}', telefone = '{novo_telefone}', materia = '{nova_materia}', idade = '{nova_idade}', cpf = '{novo_cpf}', salario = '{novo_salario}', escola = '{nova_escola}' WHERE id = {id_professor}''')

def deletar_professor(): 
    listar_professores()
    id_professor = int(input("Qual ID deseja deletar: "))
    cursor.execute(f'''DELETE FROM professor WHERE Id = {id_professor}''')
    conexao.commit()
    print("professor deletado")

def menu():
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
menu()
conexao.close()
