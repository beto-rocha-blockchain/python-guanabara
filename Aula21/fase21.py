# Interactive help

help()
print(input.__doc__)

# Docstrings

def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}',end='..')
        c+=p
    print('FIM!')

contador(2, 10, 2)

# Parâmetros opcionais

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)


# Escopo de variáveis
# Retorno de resultados

