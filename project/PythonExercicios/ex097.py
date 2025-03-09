def escreva(mensagem):
    """
    Exibe uma mensagem com um formato adaptável ao tamanho do texto.
    :param mensagem: Texto a ser exibido (string)
    """
    tamanho = len(mensagem) + 4
    print("~" * tamanho)
    print(f"  {mensagem}  ")
    print("~" * tamanho)

# Exemplo de uso
txt = input("Digite uma mensagem: ")
escreva(txt)
