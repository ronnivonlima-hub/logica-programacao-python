# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Calcula a soma de 1 até o número informado
soma = 0
for i in range(1, numero + 1):
    soma += i

# Exibe o resultado
print("A soma dos números de 1 até", numero, "é", soma)