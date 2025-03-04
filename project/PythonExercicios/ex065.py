# Variáveis para armazenar a soma, o maior e o menor valor
total_sum = 0
count = 0
largest = None
smallest = None

while True:
    # Lê um número inteiro do usuário
    num = int(input("Digite um número inteiro: "))
    
    # Atualiza a soma e o contador
    total_sum += num
    count += 1
    
    # Atualiza o maior e o menor número
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
    
    # Pergunta se o usuário quer continuar
    continue_input = input("Quer continuar? (s/n): ").strip().lower()
    if continue_input != 's':
        break  # Se a resposta não for 's', o loop será interrompido

# Calcula a média
if count > 0:
    average = total_sum / count
    print(f"\nMédia dos valores digitados: {average:.2f}")
    print(f"Maior valor digitado: {largest}")
    print(f"Menor valor digitado: {smallest}")
else:
    print("Nenhum número foi digitado.")
