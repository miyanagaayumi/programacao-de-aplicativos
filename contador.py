print("---- CONTADOR DE CICLOS DA INDÚSTRIA ----")
total_garrafas = int(input("digite o numero total de garrafas: "))



#alerta de limpeza
if total_garrafas % 500 == 0:
    print("HORA DA LIMPEZA: Parar máquina imediatamente!")

#controle de qualidade
elif total_garrafas % 100 == 0:
    print("QUALIDADE: Retirar amostra para teste.")
    
#caso tenha erro na produção
if total_garrafas % 500 != 0 and total_garrafas % 100 != 0:
    print(f"Produção em dia. Garrafa numero {total_garrafas} processada.")
    

