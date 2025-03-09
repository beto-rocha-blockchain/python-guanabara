matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna3 = 0
maior_valor_linha2 = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))
        
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        
        if j == 2:
            soma_coluna3 += matriz[i][j]
        
        if i == 1:
            if j == 0 or matriz[i][j] > maior_valor_linha2:
                maior_valor_linha2 = matriz[i][j]

print("\nMatriz formatada:")
for linha in matriz:
    for elemento in linha:
        print(f"{elemento:^5}", end=' ')
    print()

print(f"\nA soma de todos os valores pares digitados: {soma_pares}")
print(f"A soma dos valores da terceira coluna: {soma_coluna3}")
print(f"O maior valor da segunda linha: {maior_valor_linha2}")