# Criando uma lista vazia para armazenar os valores ordenados
valores = []

# Loop para ler 5 valores numéricos e inseri-los na posição correta
total_valores = 5
for i in range(total_valores):
    numero = float(input(f"Digite o {i+1}º número: "))  # Lendo um número do usuário
    
    # Inserindo na posição correta
    if not valores or numero > valores[-1]:
        valores.append(numero)  # Adiciona no final se for o maior
        posicao = len(valores) - 1
    else:
        for j in range(len(valores)):
            if numero <= valores[j]:
                valores.insert(j, numero)
                posicao = j
                break
    
    print(f"Número {numero} inserido na posição {posicao}.")

# Exibindo os valores armazenados em ordem
print("Valores armazenados em ordem:", valores)
