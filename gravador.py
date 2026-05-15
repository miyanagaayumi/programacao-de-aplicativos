import json
frase = input("Digite uma frase: ")
dados = {"mensagem": frase}
with open("teste.json", "w") as f:
    json.dump(dados, f, ensure_ascii=False)