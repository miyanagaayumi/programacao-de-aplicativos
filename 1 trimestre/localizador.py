cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
nomecidade = input("digite o nome de uma cidade: ")
if nomecidade in cidades:
    print(f"a cidade {nomecidade} esta na posição", cidades.index(nomecidade))