def main():
    # Solicitar o nome da cidade
    cidade = input("Digite o nome de uma cidade: ").strip()

    # Verificar se o nome começa com "SANTO"
    if cidade[:5].upper() == "SANTO":
        print("A cidade começa com 'SANTO'.")
    else:
        print("A cidade não começa com 'SANTO'.")

# Chama a função principal para rodar o programa
main()