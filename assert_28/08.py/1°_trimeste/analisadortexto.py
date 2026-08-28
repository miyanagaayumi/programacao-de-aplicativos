def contar_caracteres(texto):
    return len(texto)

usuario = input("digite um nome de usuario: ")
if contar_caracteres(usuario) < 5:
    print("Nome de usuário muito curto")
else: 
    print("nome aceito")