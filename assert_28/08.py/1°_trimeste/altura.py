nome = input("digite o seu nome: ")
altura = float(input("digite sua altura: "))
if altura < 1.50:
    print("Desculpe, você não tem altura minima" , nome)
elif altura >= 1.50:
    print("Acesso liberado! Divirta-se na queda livre", nome) 
