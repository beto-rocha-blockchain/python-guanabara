def main():
    # Solicitar uma frase ao usuário
    frase = input("Digite uma frase: ").strip().upper()

    # Contar quantas vezes a letra "A" aparece
    quantidade_a = frase.count("A")

    # Encontrar a posição da primeira ocorrência de "A"
    primeira_posicao = frase.find("A") + 1  # +1 para posição começar de 1

    # Encontrar a posição da última ocorrência de "A"
    ultima_posicao = frase.rfind("A") + 1  # +1 para posição começar de 1

    # Mostrar os resultados
    print(f"A letra 'A' aparece {quantidade_a} vezes na frase.")
    print(f"A primeira letra 'A' aparece na posição {primeira_posicao}.")
    print(f"A última letra 'A' aparece na posição {ultima_posicao}.")

# Chama a função principal para rodar o programa
main()
