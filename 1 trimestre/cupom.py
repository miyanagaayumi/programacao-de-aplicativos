valor_total = float(input("digite o valor total da sua compra: "))
cupom = input("digite o nome do cupom: ")

desconto = valor_total * 0.10
novo_valor = valor_total - desconto 

if cupom == "DEV10":
    print("cupom válido", novo_valor)
else:
    print("cupom inválido", valor_total)
