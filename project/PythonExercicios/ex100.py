import random

# Lista onde os números serão armazenados
números = []

# Função que sorteia 5 números e os coloca na lista
def sorteia():
    global números
    números = [random.randint(1, 100) for _ in range(5)]  # Sorteia 5 números aleatórios entre 1 e 100
    print(f"Números sorteados: {números}")

# Função que calcula a soma dos números pares sorteados
def somaPar():
    soma = sum(num for num in números if num % 2 == 0)  # Soma apenas os números pares
    print(f"A soma dos números pares sorteados é: {soma}")

# Chamando as funções
sorteia()   # Sorteia 5 números
somaPar()   # Calcula e exibe a soma dos números pares sorteados
