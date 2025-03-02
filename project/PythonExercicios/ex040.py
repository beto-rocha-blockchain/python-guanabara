# Solicita as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média
media = (nota1 + nota2) / 2

# Exibe a média do aluno
print(f"A média do aluno é: {media:.2f}")

# Determina a situação do aluno com base na média
if media < 5:
    print("Reprovado")
elif 5 <= media <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")
