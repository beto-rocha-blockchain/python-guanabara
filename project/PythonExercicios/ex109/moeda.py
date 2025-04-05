def moeda(valor):
    """Formata um número como valor monetário."""
    return f'R${valor:.2f}'.replace('.', ',')

def aumentar(valor, porcentagem, formatar=False):
    """Aumenta o valor em uma certa porcentagem."""
    resultado = valor + (valor * porcentagem / 100)
    return moeda(resultado) if formatar else resultado

def diminuir(valor, porcentagem, formatar=False):
    """Diminui o valor em uma certa porcentagem."""
    resultado = valor - (valor * porcentagem / 100)
    return moeda(resultado) if formatar else resultado

def dobro(valor, formatar=False):
    """Retorna o dobro do valor."""
    resultado = valor * 2
    return moeda(resultado) if formatar else resultado

def metade(valor, formatar=False):
    """Retorna a metade do valor."""
    resultado = valor / 2
    return moeda(resultado) if formatar else resultado