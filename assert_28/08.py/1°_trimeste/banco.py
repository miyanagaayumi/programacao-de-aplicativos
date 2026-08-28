saldo_incial = 1000.00 #variavel float 
print("seja bem vindo ao simulador bancario")
print("1 - Depósito")
print("2 - Saque")
print("3 - Extrato")
menu_de_opções = input("escolha uma das opções acima: ")

if menu_de_opções == 1: 
    depósito = float(input("digite o valor do depósito"))
    if depósito > 0.00:
        total = saldo_incial + depósito
        print("Depósito efetuado, saldo atual", total)
    else:
        print("Operação cancelada, o valor deve ser maior que zero.")

elif menu_de_opções == 2:
    saque = float(input("digite o valor que deseja sacar: "))
    if saque > 0.00 and (saque <= saldo_incial or saque == 100.00):
        total = saldo_incial - saque
        print("Saque efetuado, agora o seu saldo é", total)
    else:
        print("Saque não autorizado: Saldo insuficiente, ou valor inválido")

elif menu_de_opções == 3:
    print("Extrato: ")
    print("Saldo atual: ", saldo_incial)
else:
    print("Opção inválida")




