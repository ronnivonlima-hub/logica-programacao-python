# Listas para armazenar os dados
alunos = []
medias = []

while True:
    nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")

    if nome.lower() == "fim":
        break

    notas = []

    # Recebe as 4 notas
    for i in range(4):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        notas.append(nota)

    # Calcula a média
    media = sum(notas) / 4

    # Define a situação
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # Armazena os dados
    alunos.append([nome, media, situacao])
    medias.append(media)

# Relatório final
print("\n=== RELATÓRIO FINAL ===")

if len(alunos) > 0:
    for aluno in alunos:
        print(f"Nome: {aluno[0]}")
        print(f"Média Final: {aluno.2f}")
        print(f"Situação: {aluno[2]}")
        print("-" * 20)

    print(f"Maior média da turma: {max(medias):.2f}")
    print(f"Menor média da turma: {min(medias):.2f}")
    print(f"Média geral da turma: {sum(medias) / len(medias):.2f}")

else:
    print("Nenhum aluno foi cadastrado.")