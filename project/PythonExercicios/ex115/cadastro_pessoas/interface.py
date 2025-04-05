def linha(tam=40):
    return '-' * tam

def cabecalho(msg):
    print(f'\033[34m{linha()}\033[m')
    print(f'\033[34m{msg.center(40)}\033[m')
    print(f'\033[34m{linha()}\033[m')

def menu():
    cabecalho('MENU PRINCIPAL')
    print('\033[33m1\033[m - Ver pessoas cadastradas')
    print('\033[33m2\033[m - Cadastrar nova pessoa')
    print('\033[33m3\033[m - Apagar cadastro')
    print('\033[33m4\033[m - Sair do sistema')
    print(f'\033[34m{linha()}\033[m')

    while True:
        try:
            opcao = int(input('\033[36mSua opção: \033[m'))
            if 1 <= opcao <= 4:
                return opcao
            else:
                print('\033[31mOpção inválida. Digite de 1 a 4.\033[m')
        except ValueError:
            print('\033[31mErro: Digite um número inteiro válido.\033[m')
