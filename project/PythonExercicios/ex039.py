from datetime import date

# Solicita o ano de nascimento do usuário
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

# Calcula a idade do usuário
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

# Verifica a situação do alistamento
if idade < 18:
    print(f"Você ainda vai se alistar no serviço militar. Faltam {18 - idade} anos.")
elif idade == 18:
    print("É a hora de se alistar no serviço militar!")
else:
    print(f"Já passou do tempo do seu alistamento! Você deveria ter se alistado há {idade - 18} anos.")