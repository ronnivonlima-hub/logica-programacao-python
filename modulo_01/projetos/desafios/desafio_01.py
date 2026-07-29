usuario = input("Digite o nome do usuário: ")
salario = float(input("Digite o salário mensal: R$ "))
moradia = float(input("Digite a despesa com moradia: R$ "))
alimentacao = float(input("Digite a despesa com alimentação: R$ "))
transporte = float(input("Digite a despesa com transporte: R$ "))
outras = float(input("Digite outras despesas: R$ "))

total_despesas = moradia + alimentacao + transporte + outras
saldo_restante = salario - total_despesas
percentual_comprometido = (total_despesas / salario) * 100

print("\n================================")
print("      RELATÓRIO FINANCEIRO")
print("================================")
print(f"Usuário: {usuario}")
print(f"Salário mensal: R$ {salario:.2f}")
print(f"Moradia: R$ {moradia:.2f}")
print(f"Alimentação: R$ {alimentacao:.2f}")
print(f"Transporte: R$ {transporte:.2f}")
print(f"Outras despesas: R$ {outras:.2f}")
print(f"Total de despesas: R$ {total_despesas:.2f}")
print(f"Saldo restante: R$ {saldo_restante:.2f}")
print(f"Percentual comprometido: {percentual_comprometido:.2f}%")

print("\nComparações:")
print(f"Salário é maior que o total de despesas: {salario > total_despesas}")
print(f"Saldo restante é maior que zero: {saldo_restante > 0}")
print(f"Percentual comprometido é maior ou igual a 80%: {percentual_comprometido >= 80}")
print(f"Possui saldo positivo e comprometeu menos de 80% da renda: "
      f"{(saldo_restante > 0) and (percentual_comprometido < 80)}")