# Criando uma lista vazia para armazenar os valores
valores = []

# Loop para ler valores numéricos do usuário
while True:
    try:
        numero = float(input("Digite um número: "))
        valores.append(numero)  # Adicionando o número à lista
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
        continue
    
    continuar = input("Deseja continuar? (S/N): ").strip().lower()
    if continuar == 'n':
        break

# Exibindo informações solicitadas
print(f"A) Quantidade de números digitados: {len(valores)}")
print(f"B) Valores em ordem decrescente: {sorted(valores, reverse=True)}")
print(f"C) O valor 5 {'está' if 5 in valores else 'não está'} na lista.")
