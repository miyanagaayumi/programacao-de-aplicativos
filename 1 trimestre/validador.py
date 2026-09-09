print("---- VALIDADOR DE ANO BISSEXTO ----")
ano = input("digite se o ano é bissexto: ")

if (ano % 4 and ano != 100 ) or ano % 400: 
    print(f"O ano {ano} é bissexto!")
else: 
    print(f"O ano {ano} é um ano comum.")