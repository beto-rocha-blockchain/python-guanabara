def eh_palindromo(frase):
    frase_limpa = ''.join(caractere.lower() for caractere in frase if caractere.isalnum())
    return frase_limpa == frase_limpa[::-1]

frase = input("Digite uma frase: ")

if eh_palindromo(frase):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
