# main.py
import moeda

preco = float(input("Digite o preço: R$ "))

print(f"A metade de R$ {preco} é R$ {moeda.metade(preco):.2f}")
print(f"O dobro de R$ {preco} é R$ {moeda.dobro(preco):.2f}")
print(f"Aumentando 10%, temos R$ {moeda.aumentar(preco, 10):.2f}")
print(f"Diminuindo 13%, temos R$ {moeda.diminuir(preco, 13):.2f}")
