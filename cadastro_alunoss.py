import sqlite3 #importa a biblioteca sqlite3
conexao = sqlite3.connect('escola_demonstracao.db') #faz a conexao para o banco de dados 'escola_demonstracao.db'
cursor = conexao.cursor() #manda as informções para o banco de dados

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
''') #cria a tabela no banco de dados
print("passo 2: tabela e campos configurados")

nome_aluno = input("nome: ") #pede o nome do aluno 
idade_aluno = int(input("idade: ")) #pede a idade do aluno 
turma_alunos = input("turma: ") #pede a turma do aluno
telefone_aluno = input("telefone: ") #pede o telefone  do aluno   
cpf_aluno = input("cpf: ") #pede o cpf do aluno 

comando_inserir = (f'''
                    INSERT INTO alunos (nome, telefone, turma, idade, cpf)
                    VALUES ('{nome_aluno}', '{idade_aluno}', '{turma_alunos}', '{telefone_aluno}', '{cpf_aluno}')''') #preenche a tabela com as informações

cursor.execute(comando_inserir) #executa o comando
conexao.commit() #grava os dados no banco de dados 
conexao.close() #fecha a conexão

def listar_alunos():

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()
cursor.execute(''' SELECT * FROM alunos ''')
alunos = cursor.fetchall()
if not alunos:
    print("nenhum aluno cadastrado")
else:
    for aluno in alunos:
        print(f"id = {aluno[0]}, nome = {aluno[1]}, idade = {aluno[2]}")
conexao.close()




def alterar_nome_e_CPF():
conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

id_aluno = 1

cursor.execute("SELECT * FROM Alunos WHERE id = ?", (id_aluno,))
print(f"\nantes da alteração: {nome_aluno}")
print(cursor.fetchone())
novo_nome = "João Pedro da Silva"
novo_cpf = "123.456.789-00"
cursor.execute('''
    UPDATE Alunos
    SET nome = ?, cpf = ?
    WHERE id = ?
''', (novo_nome, novo_cpf, id_aluno))
conexao.commit()

cursor.execute("SELECT * FROM Alunos WHERE id = ?", (id_aluno,))
print("\ndepois da alteração:")
print(cursor.fetchone())

conexao.close()

