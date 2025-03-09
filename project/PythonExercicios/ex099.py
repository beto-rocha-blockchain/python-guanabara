def maior(*args):
    if len(args) == 0:
        print("Nenhum valor foi fornecido.")
        return
    maior_valor = args[0]
    for valor in args:
        if valor > maior_valor:
            maior_valor = valor
    print(f"O maior valor é: {maior_valor}")

# Testando a função com diferentes valores
maior(1, 5, 3, 9, 2)  # Exemplo com vários valores
maior(10, 20, 30, 40)  # Exemplo com outros valores
maior()  # Exemplo sem valores
