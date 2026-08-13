produtos = [
    {"nome": "Teclado", "quantidade": 10},
    {"nome": "Mouse", "quantidade": 20},
    {"nome": "Monitor", "quantidade": 5}
]

def atualizar_estoque(lista, nome_produto, nova_quantidade):
    for produto in lista:
        if produto["nome"] == nome_produto:
            produto["quantidade"] = nova_quantidade
            return True
    return False


resultado = atualizar_estoque(produtos, "Mouse", 15)

print(resultado)  
print(produtos)