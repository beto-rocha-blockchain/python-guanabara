# Solicita ao usuário dois números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Compara os números e exibe a mensagem correspondente
if numero1 > numero2:
    print("O primeiro valor é maior.")
elif numero2 > numero1:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")