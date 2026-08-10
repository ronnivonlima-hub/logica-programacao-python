# Solicita os dados ao usuário
nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")
cidade = input("Digite a cidade: ")

# Armazena os dados em um dicionário
pessoa = {
    "nome": nome,
    "email": email,
    "cidade": cidade
}

# Solicita a chave que será consultada
chave = input("Digite a chave que deseja consultar: ")

# Consulta o valor utilizando get()
valor = pessoa.get(chave)

# Verifica se a chave existe
if valor is not None:
    print(f"Valor da chave '{chave}': {valor}")
else:
    print("Dado não encontrado.")
