senha = input("digite a senha: ")
def senha_valida(senha): 
    while len(senha) < 6:
        senha = input("digite sua senha: ")
    print("senha cadastrada com sucesso!")
senha_valida(senha)
