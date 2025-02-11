# Solicita ao usuário um número inteiro
num = int(input("Digite um número inteiro: "))
 
# Exibe a tabuada do número
print(f"\nTabuada do {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")