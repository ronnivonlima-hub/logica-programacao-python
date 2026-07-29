opcao = int(input("Escolha: "))

match opcao:

    case 1:
        print("Cadastro.")

    case 2:
        print("Consulta.")

    case 3:
        print("Alteração.")

    case 4:
        print("Exclusão.")

    case _:
        print("Opção inválida.")
        