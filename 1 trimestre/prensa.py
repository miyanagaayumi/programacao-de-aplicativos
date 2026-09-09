print("----PRENSA HIDRÁULICA----")
curso  = input("digite se vc concluiu o curso de segurança: ")

if curso == "S":
    instrutor = input("O instrutor está presente na sala?")
    if instrutor == "S": 
        print("Acesso Liberado; Operação iniciada")
    else: 
        print(" Aguarde o instrutor para ligar a máquina")

else: 
    print("Acesso Negado: Faça o treinamento primeiro")
