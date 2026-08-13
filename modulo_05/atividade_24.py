
notas = []

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)


def analisar_notas(lista):
    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)
    return maior, menor, media


maior_nota, menor_nota, media_notas = analisar_notas(notas)


print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Média das notas: {media_notas:.2f}")