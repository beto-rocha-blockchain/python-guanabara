from datetime import date

# Solicita o ano de nascimento do atleta
ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))

# Calcula a idade do atleta
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

# Verifica a categoria do atleta com base na idade
if idade <= 9:
    categoria = "MIRIM"
elif idade <= 14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = "JÚNIOR"
elif idade <= 20:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"

# Exibe a categoria do atleta
print(f"O atleta tem {idade} anos e pertence à categoria {categoria}.")