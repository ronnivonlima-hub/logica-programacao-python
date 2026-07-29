# Solicitação dos dados

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: ").replace(",", "."))
peso = float(input("Digite seu peso: ").replace(",", "."))

# Exibição dos dados

print("\nDados informados:")
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Peso:", peso)

# Exibição dos tipos

print("\nTipos das variáveis:")
print(type(nome))
print(type(idade))
print(type(altura))
print(type(peso))