# Criando um dicionário para armazenar os dados do jogador
jogador = {}

# Coletando dados do jogador
jogador['nome'] = input("Nome do jogador: ")
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

# Lista para armazenar os gols de cada partida
gols_por_partida = []

# Coletando a quantidade de gols por partida
for i in range(partidas):
    gols = int(input(f"Quantos gols na partida {i + 1}? "))
    gols_por_partida.append(gols)

# Armazenando os dados no dicionário
jogador['gols'] = gols_por_partida
jogador['total'] = sum(gols_por_partida)

# Exibindo os dados do jogador
print("-=" * 20)
print(jogador)
print("-=" * 20)

# Exibindo os dados de forma mais organizada
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for i, gols in enumerate(jogador['gols']):
    print(f"   => Na partida {i + 1}, fez {gols} gols.")
print(f"Foi um total de {jogador['total']} gols no campeonato.")
