# Programa que exibe todos os números ímpares múltiplos de 3 entre 1 e 500
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:  # Verifica se o número é ímpar e múltiplo de 3
        print(i)