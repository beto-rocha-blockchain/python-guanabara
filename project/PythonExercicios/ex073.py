# Definindo a tupla com os 20 primeiros colocados do Campeonato Brasileiro
brasileirao = (
    "Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo",
    "Fluminense", "Bragantino", "São Paulo", "Internacional", "Fortaleza",
    "Cuiabá", "Corinthians", "Cruzeiro", "Santos", "Vasco da Gama",
    "Bahia", "Coritiba", "Goiás", "América-MG", "Chapecoense"
)

print('===================================================================================================')

# A) Os 5 primeiros colocados
top_5 = brasileirao[:5]
print("Os 5 primeiros colocados são:", top_5)

print('===================================================================================================')

# B) Os últimos 4 colocados da tabela
bottom_4 = brasileirao[-4:]
print("Os últimos 4 colocados são:", bottom_4)

print('===================================================================================================')

# C) Lista com os times em ordem alfabética
sorted_teams = sorted(brasileirao)
print("Times em ordem alfabética:", sorted_teams)

print('===================================================================================================')

# D) Posição da Chapecoense na tabela
pos_chapecoense = brasileirao.index("Chapecoense") + 1
print(f"A Chapecoense está na {pos_chapecoense}ª posição da tabela.")