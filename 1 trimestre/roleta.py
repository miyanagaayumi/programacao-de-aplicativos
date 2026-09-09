senha = input("digite a sua senha: ")
tentativa = int(input("digite o numero de tentativa atual: "))
token = input("digite se vc possui token: ")

if senha == "admin123" and (tentativa % 3 == 0 or token == "S"): 
    print(f"Tentativa nº {tentativa}: ACESSO CONCEDIDO.")
else:
    print(f"Tentativa nº {tentativa}: ACESSO BLOQUEADO POR PROTOCOLO. ")