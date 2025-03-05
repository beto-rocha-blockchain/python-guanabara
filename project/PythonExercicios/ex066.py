count = 0  # Contador de números digitados
total_sum = 0  # Soma total dos números

while True:
    num = int(input("Digite um número (999 para parar): "))
    
    if num == 999:
        break  # Interrompe o loop quando o número 999 é digitado
    
    count += 1  # Incrementa o contador
    total_sum += num  # Adiciona o número à soma total

# Exibe os resultados
print(f"Você digitou {count} números.")
print(f"A soma dos números digitados foi {total_sum}.")