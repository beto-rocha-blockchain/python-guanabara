def arquivo_existe(nome):
    try:
        with open(nome, 'rt'):
            return True
    except FileNotFoundError:
        return False

def criar_arquivo(nome):
    try:
        with open(nome, 'wt+') as arq:
            pass
    except:
        print('\033[31mHouve um erro ao criar o arquivo.\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso.\033[m')

def ler_arquivo(nome):
    try:
        with open(nome, 'rt') as arq:
            pessoas = arq.readlines()
            if not pessoas:
                print('\033[33mNenhum cadastro encontrado.\033[m')
            else:
                for pessoa in pessoas:
                    dado = pessoa.strip().split(';')
                    print(f'\033[32m{dado[0]:<30}\033[m {dado[1]:>3} anos')
    except:
        print('\033[31mErro ao ler o arquivo.\033[m')

def cadastrar(nome_arquivo, nome, idade):
    try:
        with open(nome_arquivo, 'at') as arq:
            arq.write(f'{nome};{idade}\n')
    except:
        print('\033[31mErro ao cadastrar a pessoa.\033[m')
    else:
        print(f'\033[32m{nome} cadastrado(a) com sucesso!\033[m')

def apagar(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arq:
            linhas = arq.readlines()

        if not linhas:
            print('\033[33mNenhuma pessoa cadastrada para apagar.\033[m')
            return

        print('\033[36mPessoas cadastradas:\033[m')
        for i, linha in enumerate(linhas):
            nome, idade = linha.strip().split(';')
            print(f'\033[33m{i+1}\033[m - {nome} ({idade} anos)')

        while True:
            try:
                escolha = int(input('\nDigite o número da pessoa que deseja apagar: '))
                if 1 <= escolha <= len(linhas):
                    break
                else:
                    print('\033[31mNúmero inválido.\033[m')
            except ValueError:
                print('\033[31mDigite um número válido.\033[m')

        removido = linhas.pop(escolha - 1)

        with open(nome_arquivo, 'w') as arq:
            arq.writelines(linhas)

        nome_removido = removido.strip().split(';')[0]
        print(f'\033[32mCadastro de {nome_removido} removido com sucesso!\033[m')

    except:
        print('\033[31mErro ao apagar cadastro.\033[m')
