frutas = ["maçã", "banana", "laranja", "uva", "abacaxi", "manga", "morango", "kiwi", "pera", "melancia"]
busca = input("digite a fruta: ")
def esta_na_lista(frutas, buscar):
    for item in frutas:
        if item == buscar: 
            return "encontrado"
    return "nao encontrado"
msg = esta_na_lista(frutas, busca)
print(msg)
