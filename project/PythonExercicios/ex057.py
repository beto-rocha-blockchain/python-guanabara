def ler_sexo():
    while True:
        sexo = input("Digite o sexo [M/F]: ").strip().upper()
        if sexo in ('M', 'F'):
            print(f"Sexo '{sexo}' registrado com sucesso!")
            return sexo
        else:
            print("Entrada inválida! Por favor, digite 'M' para masculino ou 'F' para feminino.")

# Chamando a função
ler_sexo()