from random import sample

jogos = []
quantidade = int(input("Quantos jogos deseja gerar? "))

for _ in range(quantidade):
    jogo = sorted(sample(range(1, 61), 6))
    jogos.append(jogo)

print("\nPalpites da MEGA SENA:")
for i, jogo in enumerate(jogos, 1):
    print(f"Jogo {i}: {jogo}")