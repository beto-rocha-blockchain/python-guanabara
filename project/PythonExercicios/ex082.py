# Criando listas vazias para armazenar os valores
valores = []
pares = []
impares = []

# Loop para ler valores numéricos do usuário
while True:
    try:
        numero = int(input("Digite um número: "))
        valores.append(numero)  # Adicionando o número à lista principal
        
        # Separando pares e ímpares
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
        break
    
    continuar = input("Deseja continuar? (S/N): ").strip().lower()
    if continuar == 'n':
        break

# Exibindo as listas geradas
print("Lista completa:", valores)
print("Lista de números pares:", pares)
print("Lista de números ímpares:", impares)
