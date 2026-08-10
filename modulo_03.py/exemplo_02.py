notas = []

for numero in range(5):

    nota = float(input(f"Nota {numero+1}: "))

    notas.append(nota)

media = sum(notas) / len(notas)

print(f"Média: {media:.1f}")

if media >= 7:
    print("Aprovado")

elif media >= 5:
    print("Recuperação")

else:
    print("Reprovado")