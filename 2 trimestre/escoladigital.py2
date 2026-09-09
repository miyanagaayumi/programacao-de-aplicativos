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
            alunos = json.load(f) #le um arquivo JSON e converte o conteudo para python
    else: #é caso não seja nenhum dos casos
        alunos = [] #cria uma lista vazia chamada aluno (pode adicionar as coisas depois)

    if not alunos: 
        print("Nenhum aluno cadastrado.") #mostra uma mensagem no terminal se o codigo ocorrer 
        return #encerra

    for aluno in alunos: #percorre uma lsita que seria alunos
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") #mostra a mensagem / o resultado no terminal

def atualizar():  #cria uma função que vai atualizar algo
    print("\n--- Atualizar Aluno ---")  #mostra a mensagem no terminal de forma organizada 
    if not os.path.exists(BANCO_DADOS): #pergunta se não existe dados no arquivo (BANCO_DADOS)
        print("Nenhum aluno cadastrado no sistema.") #mostra uma mensagem no terminal se o codigo ocorrer
        return #encerra

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo para uma leitura
        alunos = json.load(f) #le o arquivo JSON e coverte o conteudo para python
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) #mostra a mensagem no terminal e espera o usuario digitar a resposta
    
    for aluno in alunos: #percorre uma lsita que seria alunos
        if aluno['cpf'] == cpf_busca: #compara para saber se o cpf do aluno atual é exatamente igual ao cpf que esta procurando
            print(f"Editando dados de: {aluno['nome']}") #mostra uma mensagem no terminal se o codigo ou ação ocorrer
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] #serve para atualizar o nome do aluno, mas mantendo o nome antigo caso o usuario aperte enter sem digita nada
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] #serve para atualizar o telefone do aluno, mas mantendo o nome antigo caso o usuario aperte enter sem digita nada
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] #serve para atualizar a turma do aluno, mas mantendo o nome antigo caso o usuario aperte enter sem digita nada
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) #serve para atualizar a idade do aluno, mas mantendo o nome antigo caso o usuario aperte enter sem digita nada
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] #serve para atualizar o cpf do aluno, mas mantendo o nome antigo caso o usuario aperte enter sem digita nada
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abrimos o arquivo para escrita
                json.dump(alunos, f, indent=4, ensure_ascii=False) #grava a variavel alunos dentro de um arquivo JSON
            print("Dados atualizados com sucesso!") 
            return
            
    print("Aluno não encontrado.")

def excluir():  #cria uma função que vai excluir algo
    print("\n--- Excluir Aluno ---")  #mostra a mensagem no terminal de forma organizada 
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.") #mostra uma mensagem no terminal se o codigo ocorrer
        return #encerra

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #cria a função de deletar
        alunos = json.load(f) #le o arquivo JSON e coverte o conteudo para python
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: ")) #mostra a mensagem no terminal e espera o usuario digitar a resposta
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] #objetivo principal é filtrar uma lista, criando uma nova lista que remove um aluno especifico com base no seu id
    
    if len(nova_lista) < len(alunos): #serve para verificar se a remoção do aluno realmente aconteceu
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abrimos o arquivo para a escrita 
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) #
        print("Aluno removido com sucesso!")  #mostra a mensagem no terminal se o codigo ocorrer
    else: #caso não seja nenhum dos casos
        print("Aluno não encontrado.") ##mostra a mensagem no terminal se o codigo  nao ocorrer

def menu(): #cria uma função chamada menu
    if not os.path.exists(BANCO_DADOS): #pergunta se não existe dados no nosso arquivo
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abrimos o arquivo para escrita
            json.dump([], f) #serve para salvar uma lsita vazia dentro de um arquivo no formato JSON 

    while True: #cria um loop infinito
        print("\n=== SISTEMA ESCOLAR ===") #mostra a mensagem no terminal de uma forma organizada
        print("1. Cadastrar Aluno") #mostra a mensagem no terminal de uma forma organizada e tambem para selecionar
        print("2. Listar Alunos") #mostra a mensagem no terminal de uma forma organizada e tambem para selecionar
        print("3. Atualizar Aluno") #mostra a mensagem no terminal de uma forma organizada e tambem para selecionar
        print("4. Excluir Aluno") #mostra a mensagem no terminal de uma forma organizada e tambem para selecionar
        print("5. Sair") #mostra a mensagem no terminal de uma forma organizada e tambem para selecionar
        
        opcao = input("Escolha uma opção: ") #mostra mensagem no terminal e espera o usuario digitar
        
        if opcao == '1': cadastrar() #se a opção 1 for escolhida chama a função cadastrar e execulta essa parte do codigo
        elif opcao == '2': listar() #se a opção 2 for escolhida chama a função listar e execulta essa parte do codigo
        elif opcao == '3': atualizar() #se a opção 3 for escolhida chama a função atualizar e execulta essa parte do codigo
        elif opcao == '4': excluir() #se a opção 4 for escolhida chama a função excluir e execulta essa parte do codigo
        elif opcao == '5': break #se a opção 5 for escolhida chama a função menu e encerra o programa
        else: print("Opção inválida!") #é caso não seja nenhum dos casos, aparece no terminal "opção invalida!"

menu() #chama a função