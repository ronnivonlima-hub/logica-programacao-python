opcao = int(input("""
1 - Novo cadastro
2 - Consultar
3 - Alterar
4 - Excluir

Escolha: """))

if opcao == 1:
    print("Cadastro.")

elif opcao == 2:
    print("Consulta.")

elif opcao == 3:
    print("Alteração.")

elif opcao == 4:
    print("Exclusão.")

else:
    print("Opção inválida.")