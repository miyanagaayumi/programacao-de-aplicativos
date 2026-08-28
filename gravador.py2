import json

frase = input("digite sua mensagem: ")
dados = {
    "mensagem": frase
}
with open("teste.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False)
print("mensagem salva com sucesso em teste.json!")