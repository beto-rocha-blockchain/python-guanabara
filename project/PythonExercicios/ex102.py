def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.
    
    :param num: O número para calcular o fatorial.
    :param show: (opcional) Mostrar ou não o processo de cálculo.
    :return: O fatorial de num.
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f

# Exemplo de uso
teste1 = fatorial(5, show=True)
print(teste1)

teste2 = fatorial(7)
print(teste2)
