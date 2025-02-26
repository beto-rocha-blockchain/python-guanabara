def main():
    # Solicitar um número entre 0 e 9999
    numero = input("Digite um número entre 0 e 9999: ").zfill(4)

    # Separar as casas do número
    unidade = numero[3]
    dezena = numero[2]
    centena = numero[1]
    milhar = numero[0]

    # Mostrar os resultados
    print(f"Unidade: {unidade}")
    print(f"Dezena: {dezena}")
    print(f"Centena: {centena}")
    print(f"Milhar: {milhar}")

# Chama a função principal para rodar o programa
main()