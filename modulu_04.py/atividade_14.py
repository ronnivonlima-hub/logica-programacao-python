produtos = []

for i in range(5):
    print(f"\nCadastro do produto {i + 1}")

    nome = input("Nome: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

print("\n--- Produtos Cadastrados ---")

for produto in produtos:
    print(f"Nome: {produto['nome']}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade em estoque: {produto['quantidade']}")
    print("-" * 30)