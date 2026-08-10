# Lista para armazenar os produtos e quantidades
produtos = []

# Cadastro de 5 produtos
for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))

    produtos.append((nome, quantidade))

# Verificação do estoque
print("\nProdutos com estoque igual ou inferior a 5 unidades:")

for nome, quantidade in produtos:
    if quantidade <= 5:
        print(f"{nome} - {quantidade} unidade(s)")