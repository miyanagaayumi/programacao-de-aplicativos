nome_do_cliente = (input("digite seu nome: "))
valor_da_compra = float(input("digite o valor da sua compra: "))
distância = int(input("digite a distância em km: "))
cupom_especial = input("digite S para sim e N para não: ")
frete = 40.00

if cupom_especial == "S":
    print("seu cupom foi solicitado")
elif cupom_especial == "N":
    print("seu cupom não será solicitado")
else:
    print("ok!")

if valor_da_compra >= 1000.00 and cupom_especial == "S":
    desconto = valor_da_compra * 0.20
    total = valor_da_compra - desconto

elif valor_da_compra > 500.00 and valor_da_compra < 1000.00 and cupom_especial == "S":
    desconto = valor_da_compra * 0.10
    total =  valor_da_compra - desconto 

if distância <= 50 and total > 200.00 :
    frete = 0.00
    total_final =  total + frete 
else:
    total_final = total + frete

print(nome_do_cliente)
print(valor_da_compra)
print(desconto)
print(total_final)