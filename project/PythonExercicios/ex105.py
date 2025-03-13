def notas(*notas_alunos, situacao=False):
    """
    Função que recebe várias notas de alunos e retorna um dicionário com informações sobre as notas.
    
    Parâmetros:
    notas_alunos (float): Notas dos alunos (pode-se passar várias notas separadas por vírgula).
    situacao (bool): Se True, a função também retornará a situação dos alunos (opcional).

    Retorna:
    dict: Dicionário com as seguintes informações:
        - Quantidade de notas
        - Maior nota
        - Menor nota
        - Média da turma
        - Situação (opcional)
    """
    if len(notas_alunos) == 0:
        return "Nenhuma nota fornecida"
    
    # Calculando as informações
    quantidade = len(notas_alunos)
    maior = max(notas_alunos)
    menor = min(notas_alunos)
    media = sum(notas_alunos) / quantidade
    
    # Criando o dicionário de resultados
    resultado = {
        "Quantidade de notas": quantidade,
        "Maior nota": maior,
        "Menor nota": menor,
        "Média da turma": media
    }
    
    # Verificando a situação, se necessário
    if situacao:
        if media >= 7:
            resultado["Situação"] = "Aprovado"
        elif media >= 5:
            resultado["Situação"] = "Recuperação"
        else:
            resultado["Situação"] = "Reprovado"
    
    return resultado

# Exemplo de uso:
resultado = notas(5.5, 7.0, 8.5, 6.0, situacao=True)
print(resultado)
