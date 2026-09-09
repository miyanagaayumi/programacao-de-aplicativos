def eh_par(numero):
    return numero % 2 == 0 
numero = float(input("digite o numero: "))
if eh_par(numero):
    print("esse numero é par")
else:
    print("este numero é impar")