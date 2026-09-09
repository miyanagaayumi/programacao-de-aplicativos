print("---- FASE DE IDENTIFICAÇÃO ----")
codigo = int(input("digite o codigo do drone: "))
autorização = input("o drone possui autorização de torre:")

if codigo == 999 or autorização == "S":
    print("tudo certo! iremos avançar para analise de pouso.")
    print("---- FASE DE ANÁLISE DE VOO ----")
    bateria = int(input("digite o nível de bateria: "))
    clima = input("digite como está o clima: ")
    vento = float(input("digite a velocidade do vento em km/h: "))

    if bateria < 10:
        print("pouse imediatamente")
    elif bateria >= 10:
        if clima == "ensolarado" and vento < 30 or clima == "chuvoso" and vento < 10:
            print("pouso autorizado: iniciando descida.")
        else:
            print("POUSO NEGADO: Condiçõesd meteorológicas perigosas. Aguardando em órbita.")

else:
    print("drone não identificado, retorne a  base.")
