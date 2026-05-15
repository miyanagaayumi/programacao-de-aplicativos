{"matematica": 8.5, "portugues": 9.0}

import json

with open("notas.json", "r") as f:
    dados = json.load(f)

soma = dados["matematica"] + dados["portugues"]

print("Soma das notas:", soma)