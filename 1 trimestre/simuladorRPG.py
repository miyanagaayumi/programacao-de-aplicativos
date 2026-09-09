vida_inicial = 45000
dano = 0 
def sofrer_dano(vida_inicial, dano):
    while vida_inicial != 0:
        dano = int(input)
        vida_inicial = vida_inicial - dano
        print(f"saldo atual atualizado: {vida_inicial}")
    print("game over")
    sofrer_dano(vida_inicial, dano)