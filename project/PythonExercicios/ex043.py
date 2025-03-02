# Solicita o peso e a altura da pessoa
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o IMC e o status de acordo com o valor calculado
print(f"O IMC da pessoa é: {imc:.2f}")

if imc < 18.5:
    print("Status: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Status: Peso ideal")
elif 25 <= imc < 30:
    print("Status: Sobrepeso")
elif 30 <= imc < 40:
    print("Status: Obesidade")
else:
    print("Status: Obesidade mórbida")