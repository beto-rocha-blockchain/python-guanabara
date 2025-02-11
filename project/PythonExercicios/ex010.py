# Solicita ao usuário o valor em reais
reais = float(input("Digite quanto você tem na carteira (R$): "))

# Define a taxa de câmbio do dólar (valor pode variar)
taxa_dolar = 4.95  # Atualize conforme a cotação do momento

# Converte o valor para dólares
dolares = reais / taxa_dolar

# Exibe o resultado
print(f"Com R$ {reais:.2f}, você pode comprar aproximadamente US$ {dolares:.2f}.")