def criar_arquivo()
    open('viagens.txt', 'w').close()

def criar():
    lugar = input("destino: ")
    with open('viagens.txt', 'a') as v:
        f.write(lugar + '\n')
    print("viagem cadastrada!")
criar()
 
 def ler():
    with open('viagens.txt', 'r') as v:
        lugar = f.readlines()
