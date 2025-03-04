def progressao_aritmetica():
    while True:
        try:
            primeiro_termo = int(input("Digite o primeiro termo da PA: "))
            razao = int(input("Digite a razão da PA: "))
            break
        except ValueError:
            print("Entrada inválida! Digite números inteiros.")
    
    contador = 0
    termo_atual = primeiro_termo
    total_termos = 10
    
    while True:
        temp_contador = 0
        while temp_contador < total_termos:
            print(termo_atual, end=' ')
            termo_atual += razao
            temp_contador += 1
        print()
        
        while True:
            try:
                entrada = input("Quantos termos a mais deseja mostrar? ").strip().lower()
                if entrada in ["0", "sair", "nenhum", "parar", "não quero mais", "nao quero mais", "nada"]:
                    print("Programa encerrado.")
                    return
                mais_termos = int(entrada)
                if mais_termos >= 0:
                    break
                else:
                    print("Por favor, digite um número inteiro positivo ou 0 para sair.")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro ou uma das opções para sair.")
        
        total_termos = mais_termos

# Executando o programa
progressao_aritmetica()
