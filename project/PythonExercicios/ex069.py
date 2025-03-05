maiores_18 = 0  # Contador de pessoas com 18 anos ou mais
homens = 0  # Contador de homens cadastrados
mulheres_menos_20 = 0  # Contador de mulheres com menos de 20 anos

while True:
    print("-" * 30)
    print("CADASTRE UMA PESSOA")
    print("-" * 30)
    
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    while sexo not in ("M", "F"):  # Validação da entrada
        sexo = input("Opção inválida! Digite 'M' para masculino ou 'F' para feminino: ").strip().upper()
    
    # Verificações para as estatísticas
    if idade >= 18:
        maiores_18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    while continuar not in ("S", "N"):  # Validação da entrada
        continuar = input("Opção inválida! Digite 'S' para sim ou 'N' para não: ").strip().upper()
    
    if continuar == "N":
        break  # Sai do loop se o usuário não quiser continuar

# Exibição dos resultados
print("\n===== RESULTADOS =====")
print(f"A) Total de pessoas com 18 anos ou mais: {maiores_18}")
print(f"B) Total de homens cadastrados: {homens}")
print(f"C) Total de mulheres com menos de 20 anos: {mulheres_menos_20}")