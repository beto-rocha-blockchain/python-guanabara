print("=" * 30)
print("🟢 CAIXA ELETRÔNICO 🟢")
print("=" * 30)

valor = int(input("Digite o valor do saque: R$ "))

cedulas = [50, 20, 10, 1]  # Lista com os valores das cédulas disponíveis
distribuicao = {}  # Dicionário para armazenar a quantidade de cada cédula

for cedula in cedulas:
    quantidade = valor // cedula  # Calcula quantas cédulas desse valor são necessárias
    if quantidade > 0:
        distribuicao[cedula] = quantidade
        valor %= cedula  # Atualiza o valor restante a ser sacado

print("\n===== CÉDULAS ENTREGUES =====")
for cedula, quantidade in distribuicao.items():
    print(f"{quantidade} cédula(s) de R$ {cedula}")

print("=" * 30)
print("💰 Retire seu dinheiro com segurança! 💰")