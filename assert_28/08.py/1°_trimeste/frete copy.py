valor_da_compra = float(input("digite o valor da sua compra: "))
cliente_prime = input("digite se vc é cliente prime (S/N): ")
frete = 50.0

if valor_da_compra > 500.0 or (cliente_prime == "S" and valor_da_compra > 100.0):
    frete = 0.00
    total_com_frete = valor_da_compra + frete 