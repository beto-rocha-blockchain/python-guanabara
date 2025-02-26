def main():
    # Solicitar o nome completo da pessoa
    nome_completo = input("Digite o seu nome completo: ").strip()

    # 1. O nome com todas as letras maiúsculas
    print("Nome em maiúsculas:", nome_completo.upper())

    # 2. O nome com todas as letras minúsculas
    print("Nome em minúsculas:", nome_completo.lower())

    # 3. Quantas letras ao todo (sem considerar espaços)
    nome_sem_espacos = nome_completo.replace(" ", "")
    print("Número total de letras (sem considerar espaços):", len(nome_sem_espacos))

    # 4. Quantas letras tem o primeiro nome
    primeiro_nome = nome_completo.split()[0]
    print("Número de letras do primeiro nome:", len(primeiro_nome))

# Chama a função principal para rodar o programa
main()