
estudantes = [
    {"nome": "Ana", "idade": 20, "curso": "Engenharia"},
    {"nome": "Bruno", "idade": 22, "curso": "Administração"},
    {"nome": "Carla", "idade": 19, "curso": "Direito"}
]


nome_estudante = input("Digite o nome do estudante que deseja remover: ")


encontrado = False

for estudante in estudantes:
    if estudante["nome"].lower() == nome_estudante.lower():
        confirmacao = input(
            f"Tem certeza que deseja remover {estudante['nome']}? (s/n): "
        ).lower()

        if confirmacao == "s":
            estudantes.remove(estudante)
            print("Estudante removido com sucesso!")
        else:
            print("Remoção cancelada.")

        encontrado = True
        break


if not encontrado:
    print("Estudante não encontrado.")


print("\nRegistros restantes:")
for estudante in estudantes:
    print(
        f"Nome: {estudante['nome']}, "
        f"Idade: {estudante['idade']}, "
        f"Curso: {estudante['curso']}"
    )