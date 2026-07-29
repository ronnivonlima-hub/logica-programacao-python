print("==== MENU ====")
print("1 - Novo cadastro")
print("2 - Consultar cadastro")
print("3 - Atualizar cadastro")
print("4 - Remover cadastro")

opcao = input("Escolha uma opção: ")

match opcao:
    case "1":
        print("Você selecionou: Novo cadastro")
    case "2":
        print("Você selecionou: Consultar cadastro")
    case "3":
        print("Você selecionou: Atualizar cadastro")
    case "4":
        print("Você selecionou: Remover cadastro")
    case _:
        print("Opção inválida! Por favor, escolha uma opção de 1 a 4.")