import json #importa a biblioteca json
import os #importa a biblioteca os utilizada para os.path.exists()

BANCO_DADOS = 'alunos.json' #esta comparando que BANCO_DADOS é igual alunos.json

def cadastrar(): #cria uma função que vai cadrastrar algo
    print("\n--- Novo Cadastro ---") #mostra a mensagem no terminal de forma organizada 
    
    if os.path.exists(BANCO_DADOS): #esta perguntando se existe dados no nosso arquivo(BANCO_DADOS)
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:  #estamos abrindo o arquivo para uma leitura
            alunos = json.load(f) #lê um arquivo JSON e converte o conteúdo para Python
    else: #é caso não seja nenhum dos casos
        alunos = [] #cria uma lista vazia chamada aluno (pode adicionar as coisas depois)

    novo_aluno = { # uma variavel para armazenar algo
        "nome": input("Nome: "), #pergunta ao usuario o nome dele
        "telefone": input("Telefone: "), #pergunta ao usuario o telefone dele
        "turma": input("Turma: "), #pergunta ao usuario a turma dele
        "idade": int(input("Idade: ")), #pergunta ao usuario a idade dele
        "cpf": input("CPF: ") #pergunta ao usuario o CPF dele
    }
    
    alunos.append(novo_aluno) # adiciona um aluno a lista 

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abrimos o arquivo para escrita
        json.dump(alunos, f, indent=4, ensure_ascii=False)  #grava a variável alunos dentro de um arquivo JSON
        
    print("Aluno cadastrado com sucesso!")  #mostra uma mensagem se o código estiver certo

def listar(): #cria uma função que vai listar algo
    print("\n--- Lista de Alunos ---")  #mostra a mensagem no terminal de forma organizada 
    
    if os.path.exists(BANCO_DADOS):  #esta perguntando se existe dados no nosso arquivo(BANCO_DADOS)
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #estamos abrindo nosso arquivo para uma leitura
            alunos = json.load(f)
    else:
        alunos = []

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")

def atualizar():  #cria uma função que vai atualizar algo
    print("\n--- Atualizar Aluno ---")  #mostra a mensagem no terminal de forma organizada 
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: "))
    
    for aluno in alunos:
        if aluno['cpf'] == cpf_busca:
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            print("Dados atualizados com sucesso!")
            return
            
    print("Aluno não encontrado.")

def excluir():  #cria uma função que vai excluir algo
    print("\n--- Excluir Aluno ---")  #mostra a mensagem no terminal de forma organizada 
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    
    nova_lista = [a for a in alunos if a['id'] != id_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()