# Solicita que o usuário digite um número
numero = float(input("Digite um número: "))

# Converte o número para string e obtém a primeira parte antes do ponto decimal
parte_inteira = str(numero).split('.')[0]

# Exibe a primeira parte inteira
print(f"O número {numero} tem a parte inteira {parte_inteira}.")