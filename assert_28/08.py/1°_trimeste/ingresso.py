nome = input("digite seu nome: ")
idade = int(input("digite a sua idade: "))
ingresso_VIP = input("digite se vc tem ingresso (S/N): ")
lista = input("digite se vc esta na lista (S/N): ")

if idade > 18 and (ingresso_VIP == "S" or lista == "S"):
    print("seja bem-vindo, divirta-se", nome)
else: 
    print("acesso negado" , nome)