compras = [150.0, 80.0, 200.0, 50.0] 
desconto = []
def aplicar_promocao(lista, nova_lista):
    for item in lista:
        if item >= 100.0:
            desconto = item * 0.15
            novo_valor = item - desconto 
            nova_lista.append(novo_valor)
    print(nova_lista)

aplicar_promocao(compras, desconto)

