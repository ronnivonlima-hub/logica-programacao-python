saldo = float(input("Digite o saldo disponível: R$ "))
saque = float(input("Digite o valor do saque: R$ "))

if saque <= 0:
    print("Valor inválido! O saque deve ser maior que zero.")
elif saque <= saldo:
    saldo -= saque
    print("Saque realizado com sucesso!")
    print(f"Novo saldo: R$ {saldo:.2f}")
else:
    print("Saldo insuficiente para realizar o saque.")