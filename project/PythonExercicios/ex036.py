def aprovar_emprestimo():
    valor_casa = float(input("Digite o valor da casa: R$ "))
    salario = float(input("Digite o salário do comprador: R$ "))
    anos = int(input("Em quantos anos deseja pagar? "))
    
    meses = anos * 12
    prestacao_mensal = valor_casa / meses
    limite = salario * 0.3
    
    print(f"Para pagar uma casa de R$ {valor_casa:.2f} em {anos} anos, a prestação será de R$ {prestacao_mensal:.2f}.")
    
    if prestacao_mensal <= limite:
        print("Empréstimo APROVADO!")
    else:
        print("Empréstimo NEGADO!")

# Executar a função
aprovar_emprestimo()