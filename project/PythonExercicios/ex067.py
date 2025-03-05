while True:
    num = int(input("Digite um número para ver a tabuada (número negativo para sair): "))
    
    if num < 0:
        print("Programa encerrado. Obrigado!")
        break  # Encerra o programa se o número for negativo
    
    print(f"\nTabuada do {num}:")
    for i in range(1, 11):  # Laço para calcular a tabuada de 1 a 10
        print(f"{num} x {i} = {num * i}")
    print("-" * 20)  # Separação visual entre tabuadas