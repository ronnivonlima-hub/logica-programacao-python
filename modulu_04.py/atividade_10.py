# Solicita os dados do usuário
nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade em estoque: "))

# Cria o dicionário
produto = {
    "nome": nome,
    "preco": preco,
    "quantidade": quantidade
}

# Adiciona a categoria
produto["categoria"] = input("Digite a categoria do produto: ")

# Atualiza o preço
novo_preco = float(input("Digite o novo preço do produto: "))
produto["preco"] = novo_preco

# Aumenta a quantidade em estoque
adicional = int(input("Digite a quantidade a ser adicionada ao estoque: "))
produto["quantidade"] += adicional

# Exibe os dados atualizados
print("\nDados atualizados do produto:")
print("Nome:", produto["nome"])
print("Preço: R$", produto["preco"])
print("Quantidade em estoque:", produto["quantidade"])
print("Categoria:", produto["categoria"])