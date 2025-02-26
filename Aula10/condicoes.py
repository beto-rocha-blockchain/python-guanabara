# if carro.esquerda():
    # bloco True
# else:
    #bloco False


tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

# Condição simlificada

tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')