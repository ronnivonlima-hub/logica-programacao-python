# Lista para armazenar os nomes dos alunos
alunos = []

# Solicita o nome de 5 alunos
for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    alunos.append(nome)

# Exibe os nomes cadastrados
print("\nAlunos cadastrados:")
for aluno in alunos:
    print(aluno)