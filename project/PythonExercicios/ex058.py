import random

def jogo_adivinhacao():
    numero_secreto = random.randint(0, 10)
    tentativas = 0
    acertou = False
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número que estou pensando, entre 0 e 10.")
    
    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            if 0 <= palpite <= 10:
                tentativas += 1
                if palpite == numero_secreto:
                    acertou = True
                elif palpite < numero_secreto:
                    print("Tente um número maior.")
                else:
                    print("Tente um número menor.")
            else:
                print("Por favor, digite um número entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro entre 0 e 10.")
    
    print("\nParabéns! Você acertou o número {} após {} tentativas.".format(numero_secreto, tentativas))

# Executando o jogo
jogo_adivinhacao()