produtos = []

# Cadastro dos produtos
while True:
    produto = input("Digite o nome do produto (ou 'fim' para encerrar o cadastro): ")

    if produto.lower() == "fim":
        break

    produtos.append(produto)

# Consultas
while True:
    busca = input("\nDigite o produto que deseja consultar (ou 'fim' para sair): ")

    if busca.lower() == "fim":
        print("Programa encerrado.")
        break

    if busca in produtos:
        posicao = produtos.index(busca)
        print(f"Produto encontrado na posição {posicao}.")
    else:
        print("Produto não cadastrado.")