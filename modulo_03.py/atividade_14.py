# Lista para armazenar os produtos
produtos = []

# Cadastro de 10 produtos
for i in range(10):
    produto = input(f"Digite o nome do {i + 1}º produto: ")
    produtos.append(produto)

# Ordenação alfabética
produtos.sort()

# Exibição dos produtos
print("\nProdutos cadastrados em ordem alfabética:")
for produto in produtos:
    print(produto)