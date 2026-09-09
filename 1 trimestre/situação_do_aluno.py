def situacao_aluno(media):
    if media >= 6:
        return "aprovado"
    elif media >= 4:
        return "recuperação"
    return "reprovado"

assert situacao_aluno(9) == "aprovado"
assert situacao_aluno(6) == "aprovado"
assert situacao_aluno(4) == "recuperação"
assert situacao_aluno(2) == "reprovado"
assert situacao_aluno(5.9) == "recuperação"