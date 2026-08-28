idade = int(input("digite sua idade: "))
saldo = float(input("digite seu saldo: "))

if idade >= 18 and saldo >= 50.0: 
    print("Acesso autorizado! Bem-vindo ao evento")
elif idade < 18 and saldo < 50.0: 
    print("Infelizmente você não cumpre os requisitos de entrada.")
