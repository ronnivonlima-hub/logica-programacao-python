contatos = []

# Cadastro de contatos
quantidade = int(input("Quantos contatos deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nCadastro do contato {i + 1}")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(contato)

# Pesquisa de contato
nome_procurado = input("\nDigite o nome do contato que deseja procurar: ")

encontrado = False

for contato in contatos:
    if contato["nome"].lower() == nome_procurado.lower():
        print("\nContato encontrado:")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")
        encontrado = True
        break

if not encontrado:
    print("Contato não encontrado.")