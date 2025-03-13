def leiaint(msg):
    while True:
        try:
            n = int(input(msg))  # Tenta converter a entrada para um número inteiro
            return n
        except ValueError:  # Se ocorrer um erro de conversão (não for um número)
            print("Erro! Por favor, digite um número inteiro válido.")

# Exemplo de uso:
n = leiaint('Digite um número: ')
print(f'O número digitado foi {n}')
