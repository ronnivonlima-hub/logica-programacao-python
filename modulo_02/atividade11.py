# Lista para armazenar as notas
notas = []

# Solicita 4 notas
for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

# Calcula os resultados
maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / len(notas)

# Exibe os resultados
print("\nNotas informadas:", notas)
print("Maior nota:", maior_nota)
print("Menor nota:", menor_nota)
print("Média da turma:", media)