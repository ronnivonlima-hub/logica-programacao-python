def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):

    if b != 0:

        return a / b

    return "Erro: divisão por zero."

def divisao_inteira(a, b):
    return a // b

def resto_divisao(a, b):
    return a % b


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


print("Soma:", somar(num1, num2))
print("Subtração:", subtrair(num1, num2))
print("Multiplicação:", multiplicar(num1, num2))
print("Divisão:", dividir(num1, num2))
print("Divisão inteira:", divisao_inteira(num1, num2))
print("Resto da divisão:", resto_divisao(num1, num2))