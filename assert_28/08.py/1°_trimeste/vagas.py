vagas = ["ocupado", "livre", "ocupado", "livre"]
vagas = int(input("digite o numero de uma vaga: "))

if vagas % 2 == 0 or vagas == "livres":
    print(f"vaga autorizada para estacionar.")
else:
    print(f"vaga {indice} indisponivel ou fora das regras.")
