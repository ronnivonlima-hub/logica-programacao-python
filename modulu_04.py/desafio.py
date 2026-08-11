# Cadastro inicial do livro

livro = {
    "titulo": input("Título do livro: "),
    "autor": input("Autor: "),
    "ano": int(input("Ano de publicação: ")),
    "paginas": int(input("Quantidade de páginas: ")),
    "disponibilidade": input("Disponível? (Sim/Não): ")
}

while True:
    print("\n=== MENU ===")
    print("1 - Consultar informação")
    print("2 - Alterar valor")
    print("3 - Adicionar nova informação")
    print("4 - Remover informação")
    print("5 - Visualizar cadastro completo")
    print("6 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        chave = input("Digite a informação que deseja consultar: ")

        if chave in livro:
            print(f"{chave}: {livro.get(chave)}")
        else:
            print("Informação não encontrada.")

    elif opcao == "2":
        chave = input("Digite a informação que deseja alterar: ")

        if chave in livro:
            novo_valor = input("Digite o novo valor: ")
            livro.update({chave: novo_valor})
            print("Informação atualizada com sucesso!")
        else:
            print("Chave não encontrada.")

    elif opcao == "3":
        chave = input("Digite o nome da nova informação: ")

        if chave not in livro:
            valor = input("Digite o valor da nova informação: ")
            livro.update({chave: valor})
            print("Informação adicionada com sucesso!")
        else:
            print("Essa informação já existe.")

    elif opcao == "4":
        chave = input("Digite a informação que deseja remover: ")

        if chave in livro:
            livro.pop(chave)
            print("Informação removida com sucesso!")
        else:
            print("Chave não encontrada.")

    elif opcao == "5":
        print("\n=== CADASTRO COMPLETO ===")
        for chave, valor in livro.items():
            print(f"{chave}: {valor}")

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")