quantidade = 0
total = 0

maior_venda = 0
menor_venda = 0

while True:
    venda = float(input("Digite o valor da venda (0 para encerrar): "))

    if venda == 0:
        break

    quantidade += 1
    total += venda

    if quantidade == 1:
        maior_venda = venda
        menor_venda = venda
    else:
        if venda > maior_venda:
            maior_venda = venda

        if venda < menor_venda:
            menor_venda = venda

if quantidade > 0:
    media = total / quantidade

    print("\nResumo das vendas:")
    print("Quantidade de vendas:", quantidade)
    print("Valor total vendido: R$", total)
    print("Valor médio das vendas: R$", media)
    print("Maior venda registrada: R$", maior_venda)
    print("Menor venda registrada: R$", menor_venda)
else:
    print("Nenhuma venda foi registrada.")