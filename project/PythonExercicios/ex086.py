matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))

print("\nMatriz formatada:")
for linha in matriz:
    for elemento in linha:
        print(f"{elemento:^5}", end=' ')
    print()