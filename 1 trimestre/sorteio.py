print("---- SORTEIO DE FIDELIDADE ----")
id = input("digite o seu ID: ")
valor_da_compra = float(input("digite o valor da sua compra: "))
  
if id % 2 == 0 and valor_da_compra > 500.0:
    print("Parabéns, usuário {id}! Você ganhou um cupom para sua compra de R$ {valor}.")
else:
    print("Obrigado pela compra, usuário {id}. Continue acompanhando nossas promoções!")
