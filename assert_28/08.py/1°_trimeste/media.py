média = float(input("digite sua nota: "))
presença = int(input("digite sua presença: "))

if média >= 7.0 and presença >= 75:
    print("Parabéns! Você foi aprovado.")
elif média < 7.0 and presença < 75:
    print("Reprovado. Verifique sua nota ou frequência.") 