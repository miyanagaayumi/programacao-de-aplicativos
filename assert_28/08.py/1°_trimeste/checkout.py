def calcular_preco_final(valor, imposto_percentual, cupom):
    #imposto
    imposto = valor_base *  (imposto_percentual / 100)
    total_com_imposto = valor + valor_do_imposto

    #cupom
    preco_final = total_com_imposto - cupom 
    if preco_final < 0: 
        return 0
    else:
        return valor_base
resultado = calcular_preco_final(valor_base, imposto, cupom)

valor_base = float(input("digite o valor base: "))
valor_do_imposto = float(input("digiteo valor do imposto: "))
print(f"preco final: R$ {resultado}")