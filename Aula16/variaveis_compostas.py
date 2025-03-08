# Código errado

lanche = 'hamburguer'

lanche = 'suco'

lanche = 'pizza'

lanche = 'pudim'

# Código correto (variáveis compostas por tuplas)

# Lanche: 
# 0. Hambúrguer
# 1. Suco
# 2. Pizza
# 3. Pudim

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

print(lanche[2]) # Pizza

print(lanche[0:2]) # Hambúrguer e suco

print(lanche[1:]) # Suco, pizza e pudim

print(lanche[-1]) # Pudim

len(lanche) # responde quantos valores existem na variável (4)

for c in lanche:
    print(c)

#Para cada lanche inserido o anterior é apagado e reescrito

# As Tuplas são imutáveis!

