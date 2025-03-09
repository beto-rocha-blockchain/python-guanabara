def verifica_parenteses(texto):
    pilha = []

    for char in texto:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if len(pilha) == 0:
                return "Os parênteses não estão posicionados corretamente."
            pilha.pop()

    if len(pilha) == 0:
        return "Os parênteses existem e estão posicionados corretamente."
    else:
        return "Os parênteses não estão posicionados corretamente."

# Solicita ao usuário que insira um texto
texto_usuario = input("Digite um texto: ")

# Verifica os parênteses no texto inserido
resultado = verifica_parenteses(texto_usuario)

# Exibe o resultado da verificação
print(resultado)