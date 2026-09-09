id = int(input("digite seu id: "))
temperatura = int(input("digite a tempeeratura: "))
tempo = int(input("digite o tempo de uso: "))

if id % 3 == 0 and (temperatura > 40 or tempo > 8 ):
    print(f"Funcionario {id} vc foi escalado para manutenção hj")
else:
    print(f"funcionario {id} sua maquina opera dentro dos padrões")
    