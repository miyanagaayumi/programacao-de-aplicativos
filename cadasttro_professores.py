import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

print("1- criar")
print("2- listar")
print("3- alterar")
print("4- excluir")
print("5- sair")

def criar_professor():
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome completo TEXT NOT NULL,
        telefone TEXT,
        materia TEXT,
        idade INTEGER, 
        cpf TEXT UNIQUE NOT NULL, 
        salario REAL,
        nome da escola TEXT
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

