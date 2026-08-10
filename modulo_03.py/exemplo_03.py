produtos = []

while True:

    print()

    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Encerrar")

    opcao = input("Opção: ")

    match opcao:

        case "1":

            nome = input("Produto: ")

            produtos.append(nome)

        case "2":

            print()

            if len(produtos) == 0:

                print("Nenhum produto cadastrado.")

            else:

                for produto in produtos:
                    print(produto)

        case "3":
            break

        case _:
            print("Opção inválida.")