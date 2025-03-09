pessoas = []
soma_idade = 0

while True:
    pessoa = {}
    pessoa['nome'] = input("Nome: ")
    pessoa['sexo'] = input("Sexo [M/F]: ").strip().upper()
    while pessoa['sexo'] not in 'MF':
        print("Erro! Por favor, digite apenas M ou F.")
        pessoa['sexo'] = input("Sexo [M/F]: ").strip().upper()
    pessoa['idade'] = int(input("Idade: "))
    soma_idade += pessoa['idade']
    
    pessoas.append(pessoa)
    
    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    while continuar not in 'SN':
        print("Erro! Responda apenas S ou N.")
        continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

# Calculando a média de idade
media_idade = soma_idade / len(pessoas)

# Lista de mulheres
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']

# Pessoas com idade acima da média
acima_da_media = [p for p in pessoas if p['idade'] > media_idade]

# Exibindo os resultados
print("-=" * 20)
print(f"A) Total de pessoas cadastradas: {len(pessoas)}")
print(f"B) Média de idade do grupo: {media_idade:.2f}")
print(f"C) Lista de mulheres: {', '.join(mulheres) if mulheres else 'Nenhuma mulher cadastrada'}")
print("D) Lista de pessoas com idade acima da média:")
for p in acima_da_media:
    print(f"   Nome: {p['nome']}, Idade: {p['idade']}, Sexo: {p['sexo']}")
print("-=" * 20)