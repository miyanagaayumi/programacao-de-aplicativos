média = float(input("digite sua média: "))
renda = float(input("digite sua renda: "))
escola = str(input("digite se veio de escola pública (S/N)"))

if média > 8.0 and (renda < 2.000 or escola == "S"):
    print("Ganhou a bolsa")
else:
    print("Não atende aos requisitos")