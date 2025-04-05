import urllib.request

def testa_site(url):
    try:
        resposta = urllib.request.urlopen(url)
        # Se o código chegar aqui, o site respondeu com sucesso
        print(f'\033[32mO site {url} está acessível!\033[m')
        print(f'Status HTTP: {resposta.status}')
    except Exception as erro:
        print(f'\033[31mNão foi possível acessar o site {url}.\033[m')
        print(f'Erro: {erro}')

# Testar o site Pudim
testa_site('http://www.pudim.com.br')
