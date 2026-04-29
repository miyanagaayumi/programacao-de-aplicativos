def calcular_area(largura, comprimento):
    return largura * comprimento
for i in range(3):
    largura = float(input("largura: "))
    comprimento = float(input("comprimento: "))
    print("area:", calcular_area(largura, comprimento))