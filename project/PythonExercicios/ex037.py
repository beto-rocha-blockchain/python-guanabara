# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Exibe as opções de conversão
print("Escolha a base de conversão:")
print("1 - Para binário")
print("2 - Para octal")
print("3 - Para hexadecimal")

# Solicita ao usuário a escolha da base de conversão
opcao = int(input("Digite a opção desejada (1/2/3): "))

# Realiza a conversão com base na escolha do usuário
if opcao == 1:
    print(f"{numero} em binário é: {bin(numero)[2:]}")
elif opcao == 2:
    print(f"{numero} em octal é: {oct(numero)[2:]}")
elif opcao == 3:
    print(f"{numero} em hexadecimal é: {hex(numero)[2:]}")
else:
    print("Opção inválida! Por favor, escolha uma opção válida.")