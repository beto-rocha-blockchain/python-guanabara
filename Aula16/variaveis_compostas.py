# Código errado

lanche = hamburguer

lanche = suco

lanche = pizza

lanche = pudim

# Código correto (variáveis compostas por tuplas)

# Lanche: 
# 0. Hambúrguer
# 1. Suco
# 2. Pizza
# 3. Pudim

print(lanche[2]) # Pizza

print(lanche[0:2]) # Hambúrguer e suco

print(lanche[1:]) # Suco, pizza e hambúrguer

print(lanche[-1]) # Pudim

len(lanche) # 4

for c in lanche:
    print(c)

#Para cada lanche inserido o anterior é apagado e reescrito

# As Tuplas são imutáveis!

