def main():
    # Solicitar o nome da pessoa
    nome = input("Digite o seu nome: ").strip()

    # Verificar se o nome contém "SILVA"
    if "SILVA" in nome.upper():
        print("O nome contém 'SILVA'.")
    else:
        print("O nome não contém 'SILVA'.")

# Chama a função principal para rodar o programa
main()