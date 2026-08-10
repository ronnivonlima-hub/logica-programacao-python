# Solicita os dados do livro
titulo = input("Digite o título do livro: ")
autor = input("Digite o autor do livro: ")
ano = int(input("Digite o ano de publicação: "))
categoria = input("Digite a categoria do livro: ")

# Cria o dicionário
livro = {
    "titulo": titulo,
    "autor": autor,
    "ano": ano,
    "categoria": categoria
}

# Exibe todas as chaves
print("\nChaves do dicionário:")
print(livro.keys())

# Exibe todos os valores
print("\nValores do dicionário:")
print(livro.values())

# Exibe todos os pares chave-valor
print("\nPares chave-valor:")
print(livro.items())

# Percorre o dicionário com for e items()
print("\nInformações cadastradas:")
for chave, valor in livro.items():
    print(f"{chave}: {valor}")