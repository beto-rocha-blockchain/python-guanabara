from interface import menu, cabecalho
from arquivo import arquivo_existe, criar_arquivo, ler_arquivo, cadastrar, apagar

ARQUIVO = 'pessoas.txt'

if not arquivo_existe(ARQUIVO):
    criar_arquivo(ARQUIVO)

while True:
    opcao = menu()

    if opcao == 1:
        cabecalho('PESSOAS CADASTRADAS')
        ler_arquivo(ARQUIVO)

    elif opcao == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ').strip().title()
        while True:
            try:
                idade = int(input('Idade: '))
                break
            except ValueError:
                print('\033[31mErro: Idade deve ser um número inteiro.\033[m')
        cadastrar(ARQUIVO, nome, idade)

    elif opcao == 3:
        cabecalho('APAGAR CADASTRO')
        apagar(ARQUIVO)

    elif opcao == 4:
        cabecalho('\033[31mSaindo do sistema... Até logo!\033[m')
        break
