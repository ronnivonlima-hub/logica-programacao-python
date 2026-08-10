# Lista para armazenar os alunos
alunos = []

while True:
    print("\n=== Cadastro de Aluno ===")

    nome = input("Nome do aluno: ")

    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    nota3 = float(input("Digite a 3ª nota: "))

    # Cálculo da média
    media = (nota1 + nota2 + nota3) / 3

    # Verificação da situação
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # Armazenamento dos dados
    aluno = {
        "nome": nome,
        "notas": [nota1, nota2, nota3],
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)

    continuar = input("Deseja cadastrar outro aluno? (S/N): ").upper()

    if continuar != "S":
        break

# Relatório
print("\n" + "=" * 60)
print("RELATÓRIO FINAL")
print("=" * 60)

soma_medias = 0
aprovados = 0
medias = []

for aluno in alunos:
    print(f"\nAluno: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")

    soma_medias += aluno["media"]
    medias.append(aluno["media"])

    if aluno["situacao"] == "Aprovado":
        aprovados += 1

# Estatísticas gerais
total_alunos = len(alunos)

if total_alunos > 0:
    media_geral = soma_medias / total_alunos
    maior_media = max(medias)
    menor_media = min(medias)
    percentual_aprovados = (aprovados / total_alunos) * 100

    print("\n" + "=" * 60)
    print("ESTATÍSTICAS DA TURMA")
    print("=" * 60)
    print(f"Quantidade total de alunos: {total_alunos}")
    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Maior média: {maior_media:.2f}")
    print(f"Menor média: {menor_media:.2f}")
    print(f"Percentual de aprovados: {percentual_aprovados:.2f}%")