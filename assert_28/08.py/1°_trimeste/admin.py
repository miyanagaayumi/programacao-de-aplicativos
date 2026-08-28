usuário = input("digite seu usuário: ")
senha = int(input("digite a sua senha: "))

if (usuário == "admin" or usuário == "root") and senha == "12345":
    print("Acesso liberado!")
else:
    print("Acesso negado!")