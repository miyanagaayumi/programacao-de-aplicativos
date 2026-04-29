def somar_carrinho(precos):
    total = sum(precos)
    if total > 500.0:
        total * 0.9
lista = [300.0, 50.0, 7.0, 90.0]
print("total a pagar:", somar_carrinho(lista))