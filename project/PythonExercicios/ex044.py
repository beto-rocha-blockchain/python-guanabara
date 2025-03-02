# Solicita o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Solicita a condição de pagamento
print("Escolha a condição de pagamento:")
print("1 - À vista (dinheiro, pix ou débito)")
print("2 - À vista no cartão de crédito")
print("3 - Em até 2x no cartão de crédito")
print("4 - 3x ou mais no cartão de crédito")
condicao = int(input("Digite o número da condição de pagamento (1/2/3/4): "))

# Calcula o valor a ser pago conforme a condição de pagamento
if condicao == 1:
    # 10% de desconto para pagamento à vista (dinheiro, pix ou débito)
    valor_a_pagar = preco * 0.90
    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f} (10% de desconto)")
elif condicao == 2:
    # 5% de desconto para pagamento à vista no cartão de crédito
    valor_a_pagar = preco * 0.95
    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f} (5% de desconto)")
elif condicao == 3:
    # Em até 2x no cartão de crédito, preço normal
    valor_a_pagar = preco
    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f} (sem desconto)")
elif condicao == 4:
    # 20% de juros para 3x ou mais no cartão de crédito
    valor_a_pagar = preco * 1.20
    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f} (20% de juros)")
else:
    print("Opção inválida! Escolha uma condição de pagamento válida.")