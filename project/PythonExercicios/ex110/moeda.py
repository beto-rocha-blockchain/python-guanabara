def moeda(valor):
    """Formata um número como valor monetário."""
    return f'R${valor:.2f}'.replace('.', ',')

def aumentar(valor, porcentagem, formatar=False):
    resultado = valor + (valor * porcentagem / 100)
    return moeda(resultado) if formatar else resultado

def diminuir(valor, porcentagem, formatar=False):
    resultado = valor - (valor * porcentagem / 100)
    return moeda(resultado) if formatar else resultado

def dobro(valor, formatar=False):
    resultado = valor * 2
    return moeda(resultado) if formatar else resultado

def metade(valor, formatar=False):
    resultado = valor / 2
    return moeda(resultado) if formatar else resultado

def resumo(valor, aumento=10, reducao=5):
    """Exibe um resumo formatado do valor com seus cálculos relacionados."""
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')
    print('-' * 30)