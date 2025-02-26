frase = '   Curso em Vídeo Python   '
print(frase)
print(frase[3:13])
print(frase[:13])
print(frase[3:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print('Oi')

print("""Welcome! Are you completely new to programming?
If not then we presume you be looking for information
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!""")

print(frase.count('o')) #Conta quantos caracteres especificados existem na frase
print(frase.count('O'))

print(frase.upper().count('o')) #Conta quantos caracteres especificados transformados em maiúsculos existem na frase
print(frase.lower().count('O')) #Conta quantos caracteres especificados transformados em minúsculos existem na frase

print(len(frase)) #Conta quantos caracteres existem na frase

print(len(frase.strip())) #Conta quantos caracteres existem na frase com exceção dos espaços

print(frase.replace('Python', 'Android'))

print('Curso' in frase)

print(frase.find('Vídeo')) #Procura a palavra Vídeo dentro da frase

print(frase.lower().find('vídeo')) #Transforma todas as letras da frase em minúscula e procura a palavra

dividido = frase.split()
print(dividido[2][3])