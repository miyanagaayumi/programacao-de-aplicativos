autorizados = ["alice", "bob", "carlos"]
nome = input("digite o nome de um pesquisador: ")

#verificação de existencia
if nome in autorizados:
    print(f"acesso permitido! o pesquisador {nome} esta na posição", autorizados.index(nome))

    pergunta = input("deseja remover esse pesquisador da lista?")

    if pergunta == "s":
        autorizados.remove(nome)
        print(f"lista atualizada {autorizados}")

    else:
        print("encerrado programa!")

else:
    adicionar = input("deseja cadastrar esse novo pesquisador?")
    if adicionar == "s":
        autorizados.append(nome)
        print(f"lista atualizada {autorizados}")


