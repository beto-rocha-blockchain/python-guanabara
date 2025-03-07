# Tupla com nomes de produtos e seus respectivos preços
produtos = (
    "Arroz", 25.90,
    "Feijão", 8.50,
    "Macarrão", 5.75,
    "Óleo", 9.30,
    "Açúcar", 4.80,
    "Sal", 3.20,
    "Leite", 6.50,
    "Café", 12.90
)

# Exibindo a listagem de preços formatada
def mostrar_tabela():
    print("-" * 40)
    print(f"{'LISTAGEM DE PREÇOS':^40}")
    print("-" * 40)
    for i in range(0, len(produtos), 2):
        print(f"{produtos[i]:.<30} R$ {produtos[i+1]:>6.2f}")
    print("-" * 40)

mostrar_tabela()