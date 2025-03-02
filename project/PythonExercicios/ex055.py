maior_peso = 0
menor_peso = float('inf')

for i in range(5):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa (kg): "))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

print(f"O maior peso registrado foi: {maior_peso} kg")
print(f"O menor peso registrado foi: {menor_peso} kg")
