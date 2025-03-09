# Criando uma lista vazia para armazenar os valores
valores = []

# Loop para ler 5 valores numéricos
total_valores = 5
for i in range(total_valores):
    numero = float(input(f"Digite o {i+1}º número: "))  # Lendo um número do usuário
    valores.append(numero)  # Adicionando o número à lista

# Identificando o maior e o menor valor
maior_valor = max(valores)
menor_valor = min(valores)

# Encontrando as posições do maior e menor valor
posicoes_maior = [i for i, v in enumerate(valores) if v == maior_valor]
posicoes_menor = [i for i, v in enumerate(valores) if v == menor_valor]

# Exibindo os valores armazenados
print("Valores armazenados:", valores)
print(f"O maior valor digitado foi {maior_valor} nas posições {posicoes_maior}")
print(f"O menor valor digitado foi {menor_valor} nas posições {posicoes_menor}")