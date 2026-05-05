def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao)
    if (nota_teste > 80 and anos_xp > 2) or possui_certificacao:
        return True 
    else: 
        return False
nota = float(input("digite sua nota: "))
anos = int(input("digite os anos: "))
cert = input("digite se tem certificado: ")

possui_certificacao = cert == "s"
if verificar_aprovacao(nota, anos, possui_certificacao):
    print("contratar")
else:
    print("descartar")