# Solicita os dados ao usuário
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
cidade = input("Digite a cidade: ")
profissao = input("Digite a profissão: ")

# Armazena os dados em um dicionário
pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade,
    "profissao": profissao
}

# Exibe os dados utilizando as chaves
print("\nInformações da pessoa:")
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
print("Profissão:", pessoa["profissao"])