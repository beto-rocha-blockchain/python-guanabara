# Solicita a distância da viagem ao usuário
distancia = float(input("Digite a distância da viagem em km: "))

# Define os valores das tarifas
tarifa_curta = 0.50  # Para viagens até 200 km
tarifa_longa = 0.45  # Para viagens acima de 200 km

# Calcula o preço da passagem com base na distância
if distancia <= 200:
    preco = distancia * tarifa_curta
else:
    preco = distancia * tarifa_longa

# Exibe o valor da passagem
print(f"O preço da passagem para {distancia:.2f} km será de R$ {preco:.2f}.")
