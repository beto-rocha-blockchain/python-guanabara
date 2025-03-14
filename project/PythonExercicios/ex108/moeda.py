# moeda.py

def aumentar(valor, percentual):
    """Aumenta o valor em uma determinada porcentagem."""
    return valor + (valor * percentual / 100)

def diminuir(valor, percentual):
    """Diminui o valor em uma determinada porcentagem."""
    return valor - (valor * percentual / 100)

def dobro(valor):
    """Retorna o dobro do valor."""
    return valor * 2

def metade(valor):
    """Retorna a metade do valor."""
    return valor / 2

def moeda(valor, simbolo="R$"):
    """Formata um número como valor monetário."""
    return f"{simbolo} {valor:.2f}".replace(".", ",")
