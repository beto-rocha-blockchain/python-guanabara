from random import randint
from time import sleep
import operator

# Criando dicionário com os resultados dos jogadores
jogo = {f'Jogador {i+1}': randint(1, 6) for i in range(4)}

print("Valores sorteados:")
for jogador, valor in jogo.items():
    print(f"{jogador} tirou {valor} no dado.")
    sleep(1)

# Ordenando os jogadores pelo valor do dado (do maior para o menor)
ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)

print("\nRanking dos jogadores:")
for i, (jogador, valor) in enumerate(ranking, start=1):
    print(f"{i}º lugar: {jogador} com {valor}")
    sleep(1)