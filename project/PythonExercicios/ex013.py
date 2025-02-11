# Solicita ao usuário o salário atual do funcionário
salario = float(input("Digite o salário do funcionário (R$): "))

# Calcula o aumento de 15%
aumento = salario * 0.15
novo_salario = salario + aumento

# Exibe o resultado
print(f"\nO salário atual é R$ {salario:.2f}.")
print(f"Com um aumento de 15%, o novo salário será R$ {novo_salario:.2f}.")