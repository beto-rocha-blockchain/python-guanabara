import moeda

preco = float(input("Digite o preço: R$ "))

print(f'Preço original: {moeda.moeda(preco)}')
print(f'Dobro do preço: {moeda.dobro(preco, formatar=True)}')
print(f'Metade do preço: {moeda.metade(preco, formatar=True)}')
print(f'Aumentando 10%: {moeda.aumentar(preco, 10, formatar=True)}')
print(f'Diminuindo 20%: {moeda.diminuir(preco, 20, formatar=True)}')
