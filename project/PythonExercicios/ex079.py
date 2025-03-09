# Criando uma lista vazia para armazenar os valores únicos
valores = []

# Loop para ler valores numéricos do usuário
while True:
    try:
        numero = float(input("Digite um número: "))
        if numero not in valores:
            valores.append(numero)  # Adicionando o número à lista apenas se não existir
        else:
            print("Valor duplicado! Não será adicionado.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
        continue
    
    continuar = input("Deseja continuar? (S/N): ").strip().lower()
    if continuar == 'n':
        break

# Exibindo os valores armazenados em ordem crescente
valores.sort()
print("Valores únicos digitados em ordem crescente:", valores)
