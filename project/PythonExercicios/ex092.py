from datetime import datetime

# Criando dicionário para armazenar os dados do trabalhador
trabalhador = {}

# Entrada de dados
trabalhador['nome'] = input("Nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
trabalhador['idade'] = datetime.now().year - ano_nascimento
trabalhador['ctps'] = int(input("Carteira de Trabalho (0 se não tiver): "))

# Se tiver carteira de trabalho, pedir mais informações
if trabalhador['ctps'] != 0:
    trabalhador['ano_contratacao'] = int(input("Ano de contratação: "))
    trabalhador['salario'] = float(input("Salário: R$ "))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['ano_contratacao'] + 35) - datetime.now().year)

# Exibindo os dados
print("\nDados do trabalhador:")
for chave, valor in trabalhador.items():
    print(f"{chave.capitalize()}: {valor}")
