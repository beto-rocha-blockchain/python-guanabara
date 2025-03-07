# Tupla com várias palavras
palavras = ("programacao", "python", "desenvolvimento", "computador", "inteligencia", "artificial")

# Exibindo as vogais de cada palavra
for palavra in palavras:
    vogais = [letra for letra in palavra if letra in "aeiou"]
    print(f"Na palavra {palavra.upper()} temos: {' '.join(vogais)}")