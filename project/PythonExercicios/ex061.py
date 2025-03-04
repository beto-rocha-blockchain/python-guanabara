def progressao_aritmetica():
    while True:
        try:
            primeiro_termo = int(input("Digite o primeiro termo da PA: "))
            razao = int(input("Digite a razão da PA: "))
            break
        except ValueError:
            print("Entrada inválida! Digite números inteiros.")
    
    contador = 0
    termo_atual = primeiro_termo
    
    print("Os 10 primeiros termos da PA são:")
    while contador < 10:
        print(termo_atual, end=' ')
        termo_atual += razao
        contador += 1
    print()

# Executando o programa
progressao_aritmetica()
