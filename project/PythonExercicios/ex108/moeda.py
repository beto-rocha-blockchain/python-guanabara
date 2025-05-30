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
