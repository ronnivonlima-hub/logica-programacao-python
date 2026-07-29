# Solicita os dados do usuário

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")

# Exibe os dados utilizando um único print() e o parâmetro sep

print(nome, idade, cidade, sep=" | ")

# Utiliza dois prints e o parâmetro end

print("Bem-vindo ", end="")
print("ao curso de Python!")