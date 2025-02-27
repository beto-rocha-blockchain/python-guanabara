# Solicita a velocidade do carro ao usuário
velocidade = float(input("Digite a velocidade do carro em km/h: "))

# Define o limite de velocidade
limite_velocidade = 80
valor_multa_por_km = 7.00

# Verifica se a velocidade ultrapassou o limite
if velocidade > limite_velocidade:
    excesso = velocidade - limite_velocidade
    multa = excesso * valor_multa_por_km
    print(f"Você foi multado! O limite é de {limite_velocidade} km/h.")
    print(f"Você excedeu o limite em {excesso:.2f} km/h.")
    print(f"O valor da multa é de R$ {multa:.2f}.")
else:
    print("Velocidade dentro do limite. Dirija com segurança!")
