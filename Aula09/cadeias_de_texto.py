# 'Curso em Vídeo Python'

frase = 'Curso em Vídeo Python'

#Fatiamento

print(frase[9:13])

#No range o último número da contagem não é printado

print(frase[9:21])

print(frase[9:21:2])

print(frase[:5])

print(frase[15:])

print(frase[9::3])

len(frase)

#Análise de string

contador = frase.count('o',0,13)
print(contador)

buscador = frase.find('deo')
print(buscador)

buscador2 = frase.find('Android')
print(buscador2)

'Curso' in frase #Localizar

substituir = frase.replace('Python','Android') #Substituição
print(substituir)

tornar_maiusculas = frase.upper() #Tornar todas maiúsculas
print(tornar_maiusculas)

tornar_minúsculas = frase.lower() #Tornar todas minúsculas
print(tornar_minúsculas)

tornar_primeira_letra_maiúscula = frase.capitalize()
print(tornar_primeira_letra_maiúscula)

tornar_primeira_letra_de_cada_palavra_maiúscula = frase.title()
print(tornar_primeira_letra_de_cada_palavra_maiúscula)