def leiaint(msg):
    """
    Lê um valor inteiro com validação.
    Rejeita entradas inválidas como letras, símbolos, vazios, ou floats.
    """
    while True:
        entrada = input(msg).strip()
        if entrada == '':
            print('\033[31mErro! Entrada vazia. Digite um número inteiro válido.\033[m')
            continue
        try:
            n = int(entrada)
            return n
        except ValueError:
            print(f'\033[31mErro! "{entrada}" não é um número inteiro válido.\033[m')

def leiaFloat(msg):
    """
    Lê um valor decimal (float) com validação.
    Aceita ponto ou vírgula como separador decimal.
    """
    while True:
        entrada = input(msg).strip().replace(',', '.')
        if entrada == '':
            print('\033[31mErro! Entrada vazia. Digite um número decimal válido.\033[m')
            continue
        try:
            n = float(entrada)
            return n
        except ValueError:
            print(f'\033[31mErro! "{entrada}" não é um número decimal válido.\033[m')


# 🧪 Execução do código
num_int = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número inteiro: {num_int}')

num_float = leiaFloat('Digite um número decimal: ')
print(f'Você digitou o número decimal: {num_float}')
