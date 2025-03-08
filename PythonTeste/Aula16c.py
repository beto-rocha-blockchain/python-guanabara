lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Solução 1
for comida in lanche:
    print(f'Eu vou comer {comida} ')

# Solução 2
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# Solução 3
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
        
print('Comi pra caramba!')