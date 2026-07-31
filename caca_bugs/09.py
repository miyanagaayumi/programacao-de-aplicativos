import sqlite3

# def atualizar_nome_aluno(id_aluno, novo_nome):
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     # o professor pediu para mudar o nome do aluno de ID 3,
#     # mas o sistema alterou o nome de TODOS os alunos do banco de dados! correção urgente: 
#     cursor.execute("UPDATE alunos SET nome = ?", (novo_nome,))

#     conexao.commit()
#     conexao.close()
    
# CORRETO

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect ('sistema_escola.db')
    cursor = conexao.cursor()
    
    cursor.execute("UPDATE alunos SET nome = ? WHERE id = ?", (novo_nome,))

    conexao.commit()
    conexao.close()

id = int(input("digite o id do aluno: "))
nome = input("digite o novo nome do aluno: ")
atualizar_nome_aluno(id, nome)