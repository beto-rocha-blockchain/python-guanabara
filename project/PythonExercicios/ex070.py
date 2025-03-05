total_gasto = 0  # Acumulador do total gasto
produtos_mais_1000 = 0  # Contador de produtos acima de R$ 1000
produto_mais_barato = ""  # Nome do produto mais barato
menor_preco = None  # Preço do produto mais barato

while True:
    print("-" * 30)
    print("CADASTRE UM PRODUTO")
    print("-" * 30)

    nome = input("Nome do produto: ").strip()
    preco = float(input("Preço: R$ "))

    # Atualiza o total gasto
    total_gasto += preco

    # Conta quantos produtos custam mais de R$ 1000
    if preco > 1000:
        produtos_mais_1000 += 1

    # Verifica o produto mais barato
    if menor_preco is None or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = nome

    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    while continuar not in ("S", "N"):  # Validação da entrada
        continuar = input("Opção inválida! Digite 'S' para sim ou 'N' para não: ").strip().upper()

    if continuar == "N":
        break  # Sai do loop se o usuário não quiser continuar

# Exibição dos resultados
print("\n===== RESULTADOS =====")
print(f"A) Total gasto na compra: R$ {total_gasto:.2f}")
print(f"B) Número de produtos que custam mais de R$ 1.000,00: {produtos_mais_1000}")
print(f"C) O produto mais barato foi '{produto_mais_barato}' que custou R$ {menor_preco:.2f}")