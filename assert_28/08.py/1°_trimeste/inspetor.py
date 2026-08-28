print("----INSPETOR DE QUALIDADE----")
comprimento = input("digite se o comprimento da peça esta entre 10cm e 12cm: ")

if comprimento == "S":
    largura = input("digite se a largura está entre 5cm e 6cm: ")
    if largura == "S":
        print("PEÇA APROVADA!")
    else:
        print("REPROVADO: problema na largura")

else:
    print("REPROVADO!, problema no comprimento")
