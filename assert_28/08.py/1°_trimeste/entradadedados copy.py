compras = []
nome = ""
while nome != "fim":
    nome = input("produtos: ")
    if nome != "fim":
        compras.append(nome)
for p in compras:
    print(f"{p}")