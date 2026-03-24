cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
cidade_do_usuario = input("digite o nome de uma cidade: ")
if cidade_do_usuario in cidades:
cidades.index(cidade_do_usuario)
print(f"a cidade {cidade_do_usuario} esta na posição {posicao}")