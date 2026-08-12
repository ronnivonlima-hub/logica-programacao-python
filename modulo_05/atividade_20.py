
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def classificar_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def exibir_resultado(media, situacao):
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


media = calcular_media(nota1, nota2, nota3)
situacao = classificar_aluno(media)


exibir_resultado(media, situacao)
