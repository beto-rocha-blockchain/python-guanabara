nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
m = (nota1 + nota2) / 2

print("A sua média foi {:.1f}".format(m))  # Exibe a média com uma casa decimal
print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')