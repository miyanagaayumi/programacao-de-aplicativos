dano = int(input("digite seu dano"))
defesa = int(input("digite sua defesa"))

dano = defesa - dano 
if dano <= defesa:
    print("O vilão bloqueou o ataque! Dano:0")
elif dano >= defesa:
    print("o vilao tomou critico")
