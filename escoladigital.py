import json

def cadrastar_aluno():
    nome = input("digite seu nome completo: ")
    cpf = float(input("digite seu CPF: "))
    telefone = int(input("digite seu telefone: "))
    turma = input("digite sua turma: ")
    idade = int(input("digite sua idade: "))

aluno = {"nome completo": nome
        "cpf": cpf
        "telefone": telefone
        "turma": turma 
        "idade": idade
}

with open ("cadastro.json", 'a') as arquivo:
    json.dump(aluno, cadastro.json, indent=4, ensure-ascii=false)
    print("")