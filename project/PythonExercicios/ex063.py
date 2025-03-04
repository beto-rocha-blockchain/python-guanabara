def fibonacci():
    while True:
        try:
            n = int(input("Quantos termos da sequência de Fibonacci deseja ver? "))
            if n <= 0:
                print("Por favor, digite um número inteiro positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
    
    termo1, termo2 = 0, 1
    contador = 0
    
    print("Sequência de Fibonacci:")
    while contador < n:
        print(termo1, end=' ')
        termo1, termo2 = termo2, termo1 + termo2
        contador += 1
    print()

# Executando o programa
fibonacci()
