# EXERCICIO 1

import sqlite3

def cadastrar_hospitais():
    conexao = sqlite3.connect('sistema_hospital.db')
    cursor = conexao.cursor()
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS hospitais (
                    id_hospital INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                    nome_hospital TEXT NOT NULL,
                    cidade_hospital TEXT NOT NULL
                    )
                ''')

    try:
        nome_hospital = input("digite o nome do hospital: ")
        cidade_hospital = input("digite a cidade que esta localizado o hopistal: ")

        comando_inserir = f'''INSERT INTO hospitais (nome_hospital, cidade_hospital)
                            VALUES('{nome_hospital}', '{cidade_hospital}')'''
        cursor.execute(comando_inserir)
        print("hospital cadastrado!")
        conexao.commit()
    except ValueError:
        print("digite apenas o nome!")
    except sqlite3.IntegrityError as e:
        print("Erro! Informações ja cadastradas!", e)



def cadastrar_medicos():
    conexao = sqlite3.connect('sistema_hospitais.db')
    cursor = conexao.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS medicos (
                    id_medico INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                    nome_medico TEXT NOT NULL,
                    crm INTEGER UNIQUE NOT NULL,
                    id_hospital INTEGER FOREIGN KEY hospitais
                    )
                ''')
    try:
        nome_medico = input("digite o seu nome: ")
        crm = int(input("digite seu CRM: "))
        id_hospital = int(input("digite o id do hospital: "))

        comando_inserir = f'''INSERT INTO medicos (nome_medico, crm, id_hospital)
                            VALUES('{nome_medico}', {crm}, {id_hospital} )'''
        cursor.execute(comando_inserir)

        print("médico cadastrado!")
        conexao.commit()

    except ValueError:
        print("Erro! digite apenas o numero do ID")
    
    finally:
        conexao.close()

cadastrar_hospitais()
cadastrar_medicos()

# EXERCICIO 2

   