# Solicita ao usuário um valor em metros
metros = float(input("Digite um valor em metros: "))

# Converte para centímetros e milímetros
centimetros = metros * 100
milimetros = metros * 1000

# Exibe os resultados
print(f"{metros} metros equivalem a {centimetros} centímetros e {milimetros} milímetros.")