def contador(inicio, fim, passo):
    # Se o passo for negativo, transforma ele em positivo
    if passo < 0:
        print("Passo negativo é interpretado como decréscimo no valor.")
        passo = abs(passo)

    # Verifica se o passo é 0
    if passo == 0:
        print("O passo não pode ser 0!")
        return

    # Realiza a contagem dependendo da direção
    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=" ")
            inicio += passo
    else:
        while inicio >= fim:
            print(inicio, end=" ")
            inicio -= passo
    print()

# a) De 1 até 10, de 1 em 1
contador(1, 10, 1)

# b) De 10 até 0, de 2 em 2
contador(10, 0, 2)

# c) Contagem personalizada (usuário define os parâmetros)
inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
passo = int(input("Digite o valor do passo: "))

contador(inicio, fim, passo)
