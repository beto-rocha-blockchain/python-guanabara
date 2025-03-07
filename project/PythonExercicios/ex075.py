# Lendo 4 valores do usuário e armazenando em uma tupla
valores = tuple(int(input(f"Digite o {i+1}º valor: ")) for i in range(4))

# a) Quantas vezes apareceu o valor 9
quantidade_nove = valores.count(9)
print(f"O número 9 apareceu {quantidade_nove} vezes.")

# b) Em que posição foi digitado o primeiro valor 3
if 3 in valores:
    posicao_tres = valores.index(3) + 1
    print(f"O primeiro número 3 foi digitado na {posicao_tres}ª posição.")
else:
    print("O número 3 não foi digitado.")

# c) Quais foram os números pares
numeros_pares = tuple(num for num in valores if num % 2 == 0)
print("Os números pares digitados foram:", numeros_pares if numeros_pares else "Nenhum número par foi digitado.")
