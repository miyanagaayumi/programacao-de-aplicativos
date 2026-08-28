nível = int(input("digite seu nível: "))
esferas = int(input("digite a quantidade de esferas coletadas: "))

if nível >= 20 and esferas > 50:
    print("Habilidade Super Salto desbloqueada!")
elif nível < 20 and esferas < 50:
    print("Requisitos insuficientes para nova habilidade.")
