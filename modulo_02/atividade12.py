# Lista de alunos cadastrados
alunos = ["Ana", "Carlos", "Maria", "Pedro", "Lucas"]

# Solicita um nome ao usuário
nome = input("Digite o nome do aluno: ")

# Verifica se o nome está na lista
if nome in alunos:
    posicao = alunos.index(nome)
    print(f"O aluno {nome} está na lista.")
    print(f"Posição: {posicao}")
else:
    print(f"O aluno {nome} não está na lista.")