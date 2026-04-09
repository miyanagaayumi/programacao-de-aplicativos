peso = float(input("digite o peso: "))
altura = float(input("digite a altura: "))

imc = peso / (altura ** 2)
if imc > 25:
    print("você esta acima do peso.")
else:

    print("você está abaixo do peso.")
