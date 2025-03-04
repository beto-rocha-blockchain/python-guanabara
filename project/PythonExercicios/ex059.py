def operacoes():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Digite números válidos.")
            continue
        
        while True:
            print("\nEscolha uma opção:")
            print("1. Somar")
            print("2. Multiplicar")
            print("3. Maior")
            print("4. Novos números")
            print("5. Sair do programa")
            
            opcao = input("Digite a opção desejada: ")
            
            if opcao == '1':
                print(f"A soma é: {num1 + num2}")
            elif opcao == '2':
                print(f"A multiplicação é: {num1 * num2}")
            elif opcao == '3':
                maior = max(num1, num2)
                print(f"O maior número é: {maior}")
            elif opcao == '4':
                print("Informe novos números...")
                break
            elif opcao == '5':
                print("Saindo do programa...")
                return
            else:
                print("Opção inválida! Escolha uma opção entre 1 e 5.")

# Executando o programa
operacoes()
