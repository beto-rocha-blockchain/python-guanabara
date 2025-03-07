import random

# Gerando cinco números aleatórios e armazenando em uma tupla
numeros = tuple(random.randint(1, 100) for _ in range(5))

# Exibindo os números gerados
print("Números gerados:", numeros)

# Exibindo o maior e o menor número
print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")