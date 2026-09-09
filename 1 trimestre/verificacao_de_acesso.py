def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False

assert pode_entrar(20) == False
assert pode_entrar(16) == True
assert pode_entrar(16) == False
assert pode_entrar(18) == False
assert pode_entrar(17) == True