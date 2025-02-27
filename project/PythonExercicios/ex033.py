# Solicita três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Determina o menor número
menor = min(num1, num2, num3)

# Determina o maior número
maior = max(num1, num2, num3)

# Exibe os resultados
print(f"O menor número é {menor}")
print(f"O maior número é {maior}")
