# Programa que lê seis números inteiros e soma apenas os pares
soma = 0

# Lê 6 números inteiros
for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    if num % 2 == 0:  # Verifica se o número é par
        soma += num

# Exibe a soma dos números pares
print(f"A soma dos números pares é: {soma}")