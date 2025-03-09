alunos = []

while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    
    continuar = input("Deseja adicionar outro aluno? (S/N): ").strip().lower()
    if continuar == 'n':
        break

print("\nBoletim")
print("=" * 30)
print(f"{'No.':<4}{'Nome':<10}{'Média':>8}")
print("-" * 30)
for i, aluno in enumerate(alunos):
    print(f"{i:<4}{aluno[0]:<10}{aluno[2]:>8.2f}")

while True:
    opcao = int(input("\nMostrar notas de qual aluno? (999 para sair): "))
    if opcao == 999:
        break
    if 0 <= opcao < len(alunos):
        print(f"Notas de {alunos[opcao][0]}: {alunos[opcao][1]}")
    else:
        print("Número inválido!")