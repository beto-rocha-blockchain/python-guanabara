def ficha(nome='', gols=0):
    # Verifica se o nome está vazio
    if nome == '':
        nome = '<desconhecido>'
    
    # Verifica se os gols são negativos, ajustando para 0, caso necessário
    if gols < 0:
        gols = 0
    
    # Exibe a ficha do jogador
    print(f'O jogador {nome} fez {gols} gol(s).')

# Solicita dados do usuário
nome = input('Nome do jogador: ')
# Tenta converter a quantidade de gols para um número inteiro
# Caso o usuário não digite um número, assume 0 gols
try:
    gols = int(input('Quantos gols ele fez? '))
except ValueError:
    gols = 0

# Chama a função ficha com os dados informados
ficha(nome, gols)