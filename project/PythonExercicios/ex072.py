numeros_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    try:
        numero = int(input("Digite um número entre 0 e 20: "))
        if 0 <= numero <= 20:
            print(f"Você digitou o número {numeros_extenso[numero]}.")
            break
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro entre 0 e 20.")