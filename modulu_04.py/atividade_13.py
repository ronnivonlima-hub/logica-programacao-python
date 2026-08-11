# Cadastro do funcionário
funcionario = {}

# Solicita os dados
funcionario["nome"] = input("Digite o nome do funcionário: ")
funcionario["cargo"] = input("Digite o cargo do funcionário: ")
funcionario["setor"] = input("Digite o setor do funcionário: ")
funcionario["salario"] = float(input("Digite o salário do funcionário: "))

# Exibe o cadastro inicial
print("\nCadastro inicial:")
print(funcionario)

# Solicita a chave a ser removida
chave = input("\nDigite o nome da chave que deseja remover: ")

# Verifica se a chave existe e remove
if chave in funcionario:
    funcionario.pop(chave)
    print(f"A chave '{chave}' foi removida com sucesso.")
else:
    print(f"A chave '{chave}' não existe no cadastro.")

# Exibe o cadastro atualizado
print("\nCadastro atualizado:")
print(funcionario)