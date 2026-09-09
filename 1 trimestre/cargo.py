cargo_do_funcionario = str(input("digite o seu cargo: "))
codigo_de_acesso = int(input("digite o seu código de acesso: "))
botão_de_emergencia = input("digite se o botão de emergencia esta pressionado: ")
epi = input("digite se o equipamento de proteção está completo: ")

if (cargo_do_funcionario == "engenheiro" or cargo_do_funcionario == "técnico") and (codigo_de_acesso == "1234" or botão_de_emergencia == "s") and epi == "s":
    print("acesso liberado")
else:
    print("acesso negado")
