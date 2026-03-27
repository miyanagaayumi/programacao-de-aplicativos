nomes = ["Ayumi", "Isadora", "Eduarda", "Maria", "melissa"]
nomes_permitidos = []
for nome in nomes: 
    if len(nome) > 5:
        nomes_permitidos.append(nome)
        print(f"{nomes_permitidos}") 
