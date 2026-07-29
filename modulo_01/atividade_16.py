# Cadastro de compra

produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário: R$ "))
quantidade = int(input("Digite a quantidade: "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

# Cálculos
subtotal = preco_unitario * quantidade
valor_desconto = subtotal * percentual_desconto / 100
total = subtotal - valor_desconto

# Variável para demonstrar operador de identidade
desconto = percentual_desconto

# Resultados
print("\n--- Resumo da Compra ---")
print(f"Produto: {produto}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Total da compra: R$ {total:.2f}")

# Comparações e verificações
print(f"Quantidade maior que zero? {quantidade > 0}")
print(f"Total maior que R$ 100,00? {total > 100}")
print(f'O nome do produto contém a letra "a"? {"a" in produto.lower()}')
print(f"Desconto é diferente de None? {desconto is not None}")