
nome = print(input('Qual o seu nome: '))
resposta = input(f'{nome}, qual é o seu jogo favorito?')
print(f"Que legal, {nome}! Você gosta de {resposta} assim como eu!")

print('Por favor, {nome}, informe os valores abaixo.')


a = print(input('Valor a: '))
b = print(input('Valor b: '))

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))