def calcular_fatorial():
    while True:
        try:
            num = int(input("Digite um número para calcular o fatorial: "))
            if num < 0:
                print("O fatorial não é definido para números negativos. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
    
    fatorial = 1
    contador = num
    
    while contador > 1:
        fatorial *= contador
        contador -= 1
    
    print(f"O fatorial de {num} é {fatorial}.")

# Executando o programa
calcular_fatorial()
