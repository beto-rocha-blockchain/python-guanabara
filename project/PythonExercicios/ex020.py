import random

# Ler os nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Criar uma lista com os nomes
alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralhar a lista aleatoriamente
random.shuffle(alunos)

# Exibir a ordem sorteada
print("A ordem de apresentação será:")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")