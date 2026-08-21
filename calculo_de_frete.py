def calcular_frete(valor_comprar):
    if valor_comprar >= 200:
        return 0
    elif valor_comprar >= 100:
        return 10
    return 20

assert calcular_frete(99.99) == 20
assert calcular_frete(100) == 10
assert calcular_frete(150) == 10
assert calcular_frete(200) == 0
assert calcular_frete(250) == 0