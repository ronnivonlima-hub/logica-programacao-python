# Lista para armazenar os produtos
produtos = []

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Encerrar")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            produto = input("Digite o nome do produto: ")
            produtos.append(produto)
            print("Produto adicionado com sucesso!")

        case 2:
            produto = input("Digite o nome do produto a remover: ")

            if produto in produtos:
                produtos.remove(produto)
                print("Produto removido com sucesso!")
            else:
                print("Produto não encontrado.")

        case 3:
            if len(produtos) == 0:
                print("Nenhum produto cadastrado.")
            else:
                print("\nProdutos cadastrados:")
                for p in produtos:
                    print("-", p)

        case 4:
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida. Tente novamente.")