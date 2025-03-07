import requests
from bs4 import BeautifulSoup

def obter_classificacao():
    url = "https://ge.globo.com/futebol/brasileirao-serie-a/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    times = []
    for item in soup.select(".tabela__equipes .tabela__equipes-nome"):
        times.append(item.get_text(strip=True))
    
    return tuple(times[:20])

times_brasileirao = obter_classificacao()

print("Os 5 primeiros colocados são:", times_brasileirao[:5])
print("Os últimos 4 colocados são:", times_brasileirao[-4:])
print("Times em ordem alfabética:", sorted(times_brasileirao))

if "Chapecoense" in times_brasileirao:
    posicao_chapecoense = times_brasileirao.index("Chapecoense") + 1
    print(f"A Chapecoense está na {posicao_chapecoense}ª posição da tabela.")
else:
    print("A Chapecoense não está entre os 20 primeiros colocados.")