print("------PLANEJADOR DE VIAGENS------")
print("1. adicionar destino")
print("2. listar sugestões")
print("3. editar sugestão")
print("4. remover sugestão")
print("5. sair")
open('viagens.txt', 'w').close()

opcao = input("digite a sua escolha: ")

def criar():
    lugar = input("destino: ")
    with open('viagens.txt', 'a') as v:
        v.write(lugar + '\n')
    print("viagem cadastrada!")
criar()

def ler():
    with open('viagens.txt', 'r') as v:
        lugar = v.readlines()
        i = 0
    for lugar in lugar:
    print(f"{i} - {viagem.strip()}")
        i += 1

def atualizar():
    ler()
    idx = int(input("Digite o ID do destino que deseja alterar: "))
    novo_destino = input("Novo destino: ")
    with open('viagens.txt', 'r') as v:
        linhas = v.readlines()
    linhas[idx] = novo_destino + '\n'
    with open('viagens.txt', 'w') as v: 
        v.writelines(linhas)
    print("destino atualizado!")

def deletar():
    ler()
    idx = int(input("Digite o ID do destino que deseja excluir: "))
    with open('viagens.txt', 'r') as v:
        linhas = v.readlines()
    del linhas[idx] 
    with open('viagens.txt', 'w') as v:
        v.writelines(linhas)
    print("destino removido!")

    print("programa encerrado")

    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break

