alunos = []

for numero in range(10):

    nome = input(f"Aluno {numero + 1}: ")

    alunos.append(nome)


print("Lista de alunos:")

for aluno in alunos:
    print(aluno)