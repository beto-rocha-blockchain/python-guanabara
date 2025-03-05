import random

print("Vamos jogar Par ou Ímpar!")

vitorias = 0  # Contador de vitórias consecutivas

while True:
    num_usuario = int(input("Digite um número: "))
    escolha_usuario = input("Par ou Ímpar? [P/I]: ").strip().upper()

    while escolha_usuario not in ("P", "I"):
        escolha_usuario = input("Opção inválida! Escolha Par [P] ou Ímpar [I]: ").strip().upper()

    num_computador = random.randint(0, 10)  # Número aleatório do computador
    total = num_usuario + num_computador
    resultado = "Par" if total % 2 == 0 else "Ímpar"

    print(f"\nVocê jogou {num_usuario} e o computador {num_computador}. Total de {total}, que é {resultado}.")

    if (escolha_usuario == "P" and resultado == "Par") or (escolha_usuario == "I" and resultado == "Ímpar"):
        print("Você VENCEU! 🎉\n")
        vitorias += 1
    else:
        print("Você PERDEU! 😢\n")
        break  # O jogo acaba quando o usuário perde

print(f"Fim de jogo! Você venceu {vitorias} vez(es) consecutivamente.")