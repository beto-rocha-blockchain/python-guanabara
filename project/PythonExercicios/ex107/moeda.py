def aumentar(valor, porcentagem, formatar=False):
    resultado = valor + (valor * porcentagem / 100)
    return f'R${resultado:.2f}' if formatar else resultado

def diminuir(valor, porcentagem, formatar=False):
    resultado = valor - (valor * porcentagem / 100)
    return f'R${resultado:.2f}' if formatar else resultado

def dobro(valor, formatar=False):
    resultado = valor * 2
    return f'R${resultado:.2f}' if formatar else resultado

def metade(valor, formatar=False):
    resultado = valor / 2
    return f'R${resultado:.2f}' if formatar else resultado
