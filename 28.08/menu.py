from banco import iniciar_banco
from escola import cadastrar_escolas, listar_escolas, atualizar_escolas, excluir_escolas
from turma import cadastrar_turmas, listar_turmas, atualizar_turmas, excluir_turmas
from aluno import cadastrar_alunos, listar_alunos, atualizar_alunos, excluir_alunos



def menu():
    iniciar_banco()
    opcao = 0
    while opcao != 13:
        print("\n>>> MENU <<<")
        print("\n1-Cadastrar escola")
        print("2-Listar escola")
        print("3-Atualizar escola")
        print("4-Deletar escola")
        print("\n---------------")
        print("\n5-Cadastrar turma")
        print("6-Listar turma")
        print("7-Atualizar turma")
        print("8-Deletar escola")
        print("\n---------------")
        print("\n9-Cadastrar aluno")
        print("10-Listar aluno")
        print("11-Atualizar aluno")
        print("12-Deletar aluno")
        print("\n13->>SAIR<<")

        opcao = int(input("\nDigite a opção desejada: "))

        if opcao == 1: cadastrar_escolas()
        elif opcao == 2: listar_escolas()
        elif opcao == 3: atualizar_escolas()
        elif opcao == 4: excluir_escolas()
        elif opcao == 5: cadastrar_turmas()
        elif opcao == 6: listar_turmas()
        elif opcao == 7: atualizar_turmas()
        elif opcao == 8: excluir_turmas()
        elif opcao == 9: cadastrar_alunos()
        elif opcao == 10: listar_alunos()
        elif opcao == 11: atualizar_alunos()
        elif opcao == 12: excluir_alunos()
        elif opcao == 13:
            print("~~~~ PROGRAMA ENCERRADO! ~~~~")
            break
menu()