
produtos = [
    {"nome": "Notebook", "preco": 3500.00, "quantidade": 10},
    {"nome": "Mouse", "preco": 80.00, "quantidade": 50},
    {"nome": "Teclado", "preco": 150.00, "quantidade": 30}
]


def buscar_produto(lista_produtos, nome):
    for produto in lista_produtos:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None


nome_pesquisa = input("Digite o nome do produto: ")


resultado = buscar_produto(produtos, nome_pesquisa)


if resultado is not None:
    print("Produto encontrado:")
    print(resultado)
else:
    print("Produto não encontrado.")