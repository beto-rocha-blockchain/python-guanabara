from datetime import date

ano_atual = date.today().year
menores = 0
maiores = 0

for i in range(7):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i+1}ª pessoa: "))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f"Total de pessoas maiores de idade: {maiores}")
print(f"Total de pessoas menores de idade: {menores}")
