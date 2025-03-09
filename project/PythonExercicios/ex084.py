pessoas = []
maior_peso = menor_peso = 0

while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    
    if not pessoas:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
    
    pessoas.append([nome, peso])
    
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

print(f"\nTotal de pessoas cadastradas: {len(pessoas)}")

print("Pessoas mais pesadas:")
for p in pessoas:
    if p[1] == maior_peso:
        print(f"{p[0]} com {p[1]} kg")

print("\nPessoas mais leves:")
for p in pessoas:
    if p[1] == menor_peso:
        print(f"{p[0]} com {p[1]} kg")