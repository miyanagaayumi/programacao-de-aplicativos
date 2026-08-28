nota = float(input("digite sua nota: "))
def avaliar_desempenho(nota):
    if nota >= 9:
        return "excelente"
    elif nota >= 7:
        return "bom"
    elif nota > 5:
        return "regular"
    else:
        return "insuficiente"
final = avaliar_desempenho(nota)
print(f"sua nota é: {nota}")