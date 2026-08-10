# Sistema de Cadastro de Livros

livros = []

while True:
    print("\n=== BIBLIOTECA ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Remover livro")
    print("5 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título do livro: ")
        autor = input("Autor: ")

        livro = {
            "titulo": titulo,
            "autor": autor
        }

        livros.append(livro)
        print("Livro cadastrado com sucesso!")

    elif opcao == "2":
        if not livros:
            print("Nenhum livro cadastrado.")
        else:
            print("\n--- Lista de Livros ---")
            for i, livro in enumerate(livros, start=1):
                print(f"{i}. {livro['titulo']} - {livro['autor']}")

    elif opcao == "3":
        busca = input("Digite o título do livro: ").lower()

        encontrado = False
        for livro in livros:
            if busca in livro["titulo"].lower():
                print(f"Livro encontrado: {livro['titulo']} - {livro['autor']}")
                encontrado = True

        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == "4":
        titulo_remover = input("Digite o título do livro a remover: ").lower()

        removido = False
        for livro in livros:
            if livro["titulo"].lower() == titulo_remover:
                livros.remove(livro)
                print("Livro removido com sucesso!")
                removido = True
                break

        if not removido:
            print("Livro não encontrado.")

    elif opcao == "5":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")