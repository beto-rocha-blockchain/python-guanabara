# Solicita ao usuário o preço do produto
preco = float(input("Digite o preço do produto (R$): "))

# Calcula o desconto de 5%
desconto = preco * 0.05
novo_preco = preco - desconto

# Exibe o resultado
print(f"\nO preço original do produto era R$ {preco:.2f}.")
print(f"Com 5% de desconto, o novo preço é R$ {novo_preco:.2f}.")