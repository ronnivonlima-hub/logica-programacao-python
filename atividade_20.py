#Solicite ao usuário o nome, o preço e a quantidade em estoque de um produto. Crie uma função que receba esses dados como parâmetros e retorne um dicionário representando o produto. Ao final, apresente o cadastro criado.

def criar_produto(nome, preco, estoque):
    
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }
    return produto


nome_input = input("Digite o nome do produto: ")
preco_input = float(input("Digite o preço do produto (ex: 12.50): "))
estoque_input = int(input("Digite a quantidade em estoque: "))


cadastro = criar_produto(nome_input, preco_input, estoque_input)

print("\n--- Produto Cadastrado com Sucesso ---")
print(f"Dicionário: {cadastro}")
print(f"Nome: {cadastro['nome']}")
print(f"Preço: R$ {cadastro['preco']:.2f}")
print(f"Estoque: {cadastro['estoque']} unidades")