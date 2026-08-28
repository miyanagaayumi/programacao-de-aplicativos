livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
emprestimo = input("digite o nome do livro que deseja: ")
#emprestimo
if emprestimo in livros_disponiveis:
    livros_disponiveis.remove(emprestimo)
    livros_emprestados.append(emprestimo)
    print("Empréstimo realizado com sucesso!")
else: 
    print("Desculpe, este livro não está no acervo.")
print("\n")
#devolução
devolução = input("digite o livro que vc esta devolvendo: ")
if devolução in livros_emprestados:
    livros_emprestados.remove(devolução)
    livros_disponiveis.append(devolução)
else:
    print("Este livro não consta como emprestado.")
print("\n")
#manutenção 
del livros_disponiveis[0:2]
print("estado final das listas:")
print(f"-livros disponiveis: {livros_disponiveis}")
print(f"-livros emprestados: {livros_emprestados}")