def apresentar_produto(nome, preco, estoque):
    print("\n--- Dados do Produto ---")
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque}")


#nome = input("Digite o nome do produto: ")
#preco = float(input("Digite o preço do produto: "))
#estoque = int(input("Digite a quantidade em estoque: "))


#apresentar_produto(nome, preco, estoque)

apresentar_produto(
    "Monitor",
    899.90,
    5
)