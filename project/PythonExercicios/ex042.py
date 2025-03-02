# Solicita os comprimentos das três retas
reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))

# Verifica se as retas podem formar um triângulo
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("As retas podem formar um triângulo!")
    
    # Verifica o tipo do triângulo
    if reta1 == reta2 == reta3:
        print("O triângulo formado é EQUILÁTERO.")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("O triângulo formado é ISÓSCELES.")
    else:
        print("O triângulo formado é ESCALENO.")
else:
    print("As retas NÃO podem formar um triângulo.")
