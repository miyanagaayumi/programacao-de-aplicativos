import sqlite3
# def verificar_registros ():
#     conexao = sqlite3.connect(‘ sistema_escola.db’)
#     cursor = conexao.cursor()
#     cursor. execute (“SELECT * FROM alunos”)
#     # Por que o segundo print não mostra absolutamente nada no console?
#     print( “Primeiro print:”, cursor. fetchall())
#     print (“Segundo print:”, cursor. fetchall())
#     conexao. close()

#   CORRETO

def verificar_registros ():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute ("SELECT * FROM alunos")

    dados = cursor.fetchall()
    print("Primeiro print:", dados)
    print ("Segundo print:", dados)
    conexao.close()
