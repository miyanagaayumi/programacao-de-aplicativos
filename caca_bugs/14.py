import sqlite3 

def cadastrar_serue_segundo(nome, id_escola):
    try:
        #se a linha abaixo falhar por falta de permissão na pasta,
        #o bloco 'finally' vai tentar fechar algo que não abriu. como corrigir?
        conexao = sqlite3.connect('/pasta/sistema.db')
        cursor = conexao.cursor()
        cusor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome, id_escola))
        conexao.commit()
        except sqlite3.Error as e:
            print("erro tecnico:", e)
        finally:
            conexao.close()
            