import math

# Solicita ao usuário que insira um ângulo
graus = float(input("Digite o valor do ângulo em graus: "))

# Converte o ângulo de graus para radianos
radianos = math.radians(graus)

# Calcula seno, cosseno e tangente
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

# Exibe os resultados
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente:.4f}")