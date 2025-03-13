import colorama
from colorama import Fore, Back

# Inicializando o colorama
colorama.init(autoreset=True)

def sistema_help():
    """
    Função que permite ao usuário consultar o manual interativo
    dos comandos ou bibliotecas do Python utilizando a função help().
    O programa será encerrado ao digitar 'FIM'.
    """
    print(Fore.WHITE + Back.GREEN + "Bem-vindo ao sistema de ajuda interativo do Python!")
    print(Fore.BLACK + Back.YELLOW + "Digite o nome de uma função ou biblioteca para ver o manual (ou 'FIM' para sair):")
    
    while True:
        # Solicita o comando ou nome da biblioteca
        comando = input(Fore.CYAN + Back.BLACK + "Comando/Biblioteca: ").strip()
        
        if comando.lower() == "fim":
            print(Fore.WHITE + Back.RED + "Sistema encerrado.")
            break
        
        # Exibe o manual do comando ou biblioteca utilizando a função help()
        try:
            print(Fore.MAGENTA + Back.BLACK + f"\nManual do comando/biblioteca '{comando}':")
            help(comando)
        except Exception as e:
            print(Fore.WHITE + Back.RED + f"\nErro: {str(e)}")

# Chamando a função para iniciar o sistema
sistema_help()