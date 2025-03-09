def area(largura, comprimento):
    """
    Calcula e exibe a área de um terreno retangular.
    :param largura: Largura do terreno (float ou int)
    :param comprimento: Comprimento do terreno (float ou int)
    """
    resultado = largura * comprimento
    print(f'A área do terreno de {largura}m x {comprimento}m é {resultado}m².')

# Entrada de dados pelo usuário
largura = float(input("Digite a largura do terreno (m): "))
comprimento = float(input("Digite o comprimento do terreno (m): "))

# Chamada da função
area(largura, comprimento)