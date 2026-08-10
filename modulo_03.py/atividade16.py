# Lista para armazenar os dados dos alunos
alunos = []

aprovados = 0
recuperacao = 0
reprovados = 0

# Cadastro dos 5 alunos
for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    media = float(input("Digite a média final: "))

    # Determina a situação do aluno
    if media >= 7:
        situacao = "Aprovado"
        aprovados += 1
    elif media >= 5:
        situacao = "Recuperação"
        recuperacao += 1
    else:
        situacao = "Reprovado"
        reprovados += 1

    alunos.append([nome, media, situacao])

# Relatório
print("\nRELATÓRIO DOS ALUNOS")
print("-" * 40)

for aluno in alunos:
    print(f"Nome: {aluno[0]}")
    print(f"Média: {aluno:.1f}")
    print(f"Situação: {aluno[2]}")
    print("-" * 40)

# Resumo final
print("\nRESUMO")
print(f"Quantidade de aprovados: {aprovados}")
print(f"Quantidade em recuperação: {recuperacao}")
print(f"Quantidade de reprovados: {reprovados}")