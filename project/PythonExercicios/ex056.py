total_idade = 0
homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(4):
    print(f"--- {i+1}ª PESSOA ---")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    
    total_idade += idade
    
    if sexo == 'M' and idade > idade_homem_mais_velho:
        homem_mais_velho = nome
        idade_homem_mais_velho = idade
    
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = total_idade / 4

print(f"A média de idade do grupo é {media_idade:.1f} anos.")
print(f"O homem mais velho é {homem_mais_velho} com {idade_homem_mais_velho} anos.")
print(f"No grupo, há {mulheres_menos_20} mulher(es) com menos de 20 anos.")