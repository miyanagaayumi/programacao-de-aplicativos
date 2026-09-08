import banco
import escola
import turma
import aluno


def menu_escolas():
    while True:
        print("\n===== MENU ESCOLAS =====")
        print("1 - cadastrar escola")
        print("2 - listar escolas")
        print("3 - sair")
        
        opcao = input("escolha uma opção: ")

        if opcao == "1":
            nome = input("nome da escola: ")
            cidade = input("cidade: ")

            try:
                escola.cadastrar_escola(nome, cidade)
            except AssertionError as erro:
                print(f"Validação: {erro}")

        elif opcao == "2":
            escola.listar_escolas()

        elif opcao == "3":
            break

        else:
            print("Opção inválida.")


def menu_turmas():
    while True:
        print("\n===== MENU TURMAS =====")
        print("1 - cadastrar turma")
        print("2 - listar turmas")
        print("3 - sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da turma: ")
            id_escola = ler_inteiro("ID da escola: ")

            if id_escola is None:
                continue

            try:
                turma.cadastrar_turma(nome, id_escola)
            except AssertionError as erro:
                print(f"Validação: {erro}")

        elif opcao == "2":
            turma.listar_turmas()

        elif opcao == "3":
            break

        else:
            print("Opção inválida.")


def menu_alunos():
    while True:
        print("\n===== MENU ALUNOS =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - sair")
        print("4 - Excluir aluno")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            idade = ler_inteiro("Idade: ")

            if idade is None:
                continue

            id_turma = ler_inteiro("ID da turma: ")

            if id_turma is None:
                continue

            try:
                aluno.cadastrar_aluno(
                    nome,
                    idade,
                    id_turma
                )
            except AssertionError as erro:
                print(f"Validação: {erro}")

        elif opcao == "2":
            aluno.listar_alunos()

        elif opcao == "3":
            id_aluno = ler_inteiro("ID do aluno: ")

            if id_aluno is None:
                continue

            nome = input("Novo nome: ")
            idade = ler_inteiro("Nova idade: ")

            if idade is None:
                continue

            id_turma = ler_inteiro("Novo ID da turma: ")

            if id_turma is None:
                continue

            try:
                aluno.alterar_aluno(
                    id_aluno,
                    nome,
                    idade,
                    id_turma
                )
            except AssertionError as erro:
                print(f"Validação: {erro}")

        elif opcao == "4":
            id_aluno = ler_inteiro("ID do aluno: ")

            if id_aluno is None:
                continue

            try:
                aluno.excluir_aluno(id_aluno)
            except AssertionError as erro:
                print(f"Validação: {erro}")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def iniciar():
    # Cria o banco e as tabelas antes de iniciar o sistema
    banco.criar_tabelas()

    while True:
        print("\n")
        print("==============================")
        print("     SISTEMA DE GESTÃO ESCOLAR")
        print("==============================")
        print("1 - Escolas")
        print("2 - Turmas")
        print("3 - Alunos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_escolas()

        elif opcao == "2":
            menu_turmas()

        elif opcao == "3":
            menu_alunos()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    iniciar()
