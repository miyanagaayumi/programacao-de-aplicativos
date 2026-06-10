import sqlite3 
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

print("Passo 1: Conectado ao banco de dados")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL
    )
''')
print("passo 2: tabela e campos configurados")

nome_aluno = input(nome: )
telefone_aluno = input(telefone: )
turma_alunos = input(turma: )
idade_aluno = int(idade: )
cpf_aluno = input(cpf: )

comando_inserir = (f'''
                    INSERT INTO alunos (nome, telefone, idade, cpf)
                    VALUES ('{nome_aluno}', '{telefone_aluno}', '{turma_alunos}', '{idade_aluno}', '{cpf_aluno}')''')
