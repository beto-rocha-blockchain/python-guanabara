from datetime import date

def voto(ano_nascimento):
    """
    Determina a obrigatoriedade do voto com base no ano de nascimento.
    :param ano_nascimento: Ano de nascimento da pessoa
    :return: String indicando se o voto é NEGADO, OPCIONAL ou OBRIGATÓRIO
    """
    idade = date.today().year - ano_nascimento
    
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# Exemplo de uso
ano = int(input("Em que ano você nasceu? "))
print(voto(ano))
