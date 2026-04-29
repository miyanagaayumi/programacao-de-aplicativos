def converter_km_para_ms(velocidade):
    return velocidade / 3.6
velocidade = float(input("digite a velocidade: "))
if velocidade > 80:
    print("velocidade em ms:", converter_km_para_ms(velocidade))
    print("reduza a velocidade")
