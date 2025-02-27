# Solicita o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$ "))

# Define a porcentagem de aumento com base no salário
if salario > 1250:
    percentual = 10  # Aumento de 10% para salários acima de R$ 1.250
else:
    percentual = 15  # Aumento de 15% para salários de até R$ 1.250

# Calcula o valor do aumento e o novo salário
aumento = salario * (percentual / 100)
novo_salario = salario + aumento

# Exibe os resultados
print(f"O aumento será de {percentual}% (R$ {aumento:.2f}).")
print(f"O novo salário será de R$ {novo_salario:.2f}.")
