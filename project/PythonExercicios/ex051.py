import time

# Programa para mostrar os 10 primeiros termos de uma PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

total_termos = 10

tempo_estimado = total_termos * 0.00001  # Estimativa baseada no tempo médio por iteração
print(f"A execução deste programa pode levar aproximadamente {tempo_estimado:.2f} segundos.")

deseja_continuar = input("Deseja continuar? (s/n): ").strip().lower()
if deseja_continuar != 's':
    print("Operação cancelada.")
else:
    inicio = time.time()
    for i in range(total_termos):
        termo_atual = primeiro_termo + i * razao
        print(termo_atual, end=" -> ")
    print("Fim")
    fim = time.time()
    print(f"Tempo total de execução: {fim - inicio:.2f} segundos")