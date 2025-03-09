jogadores = []

while True:
    jogador = {}
    jogador['nome'] = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    
    gols_por_partida = []
    for i in range(partidas):
        gols = int(input(f"Quantos gols na partida {i + 1}? "))
        gols_por_partida.append(gols)
    
    jogador['gols'] = gols_por_partida
    jogador['total'] = sum(gols_por_partida)
    jogadores.append(jogador)
    
    continuar = input("Quer adicionar outro jogador? [S/N]: ").strip().upper()
    while continuar not in 'SN':
        print("Erro! Responda apenas S ou N.")
        continuar = input("Quer adicionar outro jogador? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

print("-=" * 30)
print(f"{'Cod':<4}{'Nome':<15}{'Total de Gols':<15}")
print("-" * 30)
for i, jogador in enumerate(jogadores):
    print(f"{i:<4}{jogador['nome']:<15}{jogador['total']:<15}")

while True:
    print("-=" * 30)
    opc = int(input("Mostrar dados de qual jogador? (999 para sair): "))
    if opc == 999:
        break
    if 0 <= opc < len(jogadores):
        jogador = jogadores[opc]
        print(f"-- Levantamento do jogador {jogador['nome']}: ")
        for i, gols in enumerate(jogador['gols']):
            print(f"   => No jogo {i + 1}, fez {gols} gols.")
    else:
        print("Erro! Código inválido.")
print("<< PROGRAMA ENCERRADO >>")