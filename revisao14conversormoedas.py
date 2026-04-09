taxa = 5.0  # R$ 5,00 = US$ 1,00
reais = float(input("digite o valor em reais: "))
dolares = reais / taxa
print(f"Valor em dólares: US$ {dolares:.2f}")