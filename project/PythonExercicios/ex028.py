import random

# Computador escolhe um número aleatório entre 0 e 5
numero_computador = random.randint(0, 5)

# Usuário tenta adivinhar o número
numero_usuario = int(input("Tente adivinhar o número entre 0 e 5 que o computador escolheu: "))

# Verifica se o usuário acertou
if numero_usuario == numero_computador:
    print("Parabéns! Você acertou!")
else:
    print(f"Que pena! O número correto era {numero_computador}. Tente novamente!")
