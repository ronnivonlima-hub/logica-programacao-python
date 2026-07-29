cliente = input("Digite o nome do cliente: ")
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))
percentual = float(input("Digite o percentual de desconto: "))

subtotal = preco * quantidade
desconto = subtotal * percentual / 100
total = subtotal - desconto

print("================================")
print("        RESUMO DA COMPRA")
print("================================")
print(f"Cliente: {cliente}")
print(f"Produto: {produto}")
print(f"Preço unitário: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total: R$ {total:.2f}")