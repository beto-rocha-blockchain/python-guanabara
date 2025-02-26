def main():
    # Solicitar o nome completo da pessoa
    nome_completo = input("Digite seu nome completo: ").strip()

    # Dividir o nome em partes
    partes_nome = nome_completo.split()

    # Obter o primeiro e o último nome
    primeiro_nome = partes_nome[0]
    ultimo_nome = partes_nome[-1]

    # Mostrar os resultados
    print(f"Primeiro nome: {primeiro_nome}")
    print(f"Último nome: {ultimo_nome}")

# Chama a função principal para rodar o programa
main()