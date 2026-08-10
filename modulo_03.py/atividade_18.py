notas = []

# Cadastro das notas
for i in range(10):
    nota = float(input(f"Digite a nota do {i+1}º estudante: "))
    notas.append(nota)

# Ordem crescente
print("\nNotas em ordem crescente:")
print(sorted(notas))

# Ordem decrescente
print("\nNotas em ordem decrescente:")
print(sorted(notas, reverse=True))

# Maior nota
print(f"\nMaior nota: {max(notas)}")

# Menor nota
print(f"Menor nota: {min(notas)}")

# Média da turma
media = sum(notas) / len(notas)
print(f"Média da turma: {media:.2f}")