def leiaDinheiro(msg):
    """
    Lê um valor digitado e valida se é um valor monetário.
    Aceita entradas como: 1000, 25.50, 49,90 (com vírgula ou ponto)
    """
    while True:
        entrada = input(msg).strip().replace(',', '.')
        
        if entrada.replace('.', '', 1).isdigit():
            return float(entrada)
        else:
            print(f'\033[31mERRO: "{entrada}" não é um valor monetário válido.\033[m')