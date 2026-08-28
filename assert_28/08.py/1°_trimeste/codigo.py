nome_de_usuário = input("digite seu nome de usuário: ")
código_de_segurança = float(input("digite seu código de segurança: "))

if nome_de_usuário == "admin" and código_de_segurança == 999:
    print("Acesso ao servidor liberado. Sistema online.")
else: 
    print("Falha na autenticação. Alerta de segurança ativado!")