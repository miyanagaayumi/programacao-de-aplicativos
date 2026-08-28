codigo = int(input("digite o codigo do pacote: "))
peso = float(input("digite o peso do pacote: "))

if peso > 50:
    status = "carga pesada"
elif peso < 5 and codigo % 10 == 0: 
    status = "entrega expressa"
else:
    status = "entrega normal"

print(f"pacote {codigo}: {status}") 