print("----ESTUFA INTELIGENTE----")
temperatura_atual = float(input("digite a temperatura atual: "))

if temperatura_atual <= 30.0:
    print("Clima estável")

elif temperatura_atual > 30.0:
    print("Alerta de Calor!")
    umidade = float(input("digite a umidade: "))
    if umidade < 40.0:
        print("Ação: Ligar Irrigação!")
    else:
        print("Ação: Ligar apenas ventiladores")
            