def cadastrar_produto(nome, preco, quantidade):
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade_estoque": quantidade
    }
    return produto


nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade em estoque: "))


produto_cadastrado = cadastrar_produto(nome, preco, quantidade)


print("\nCadastro do Produto:")
print(produto_cadastrado)

