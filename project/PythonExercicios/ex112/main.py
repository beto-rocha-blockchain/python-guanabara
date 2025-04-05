from utilidadesCeV import moeda, dado

preco = dado.leiaDinheiro("Digite o preço: R$ ")
moeda.resumo(preco, aumento=10, reducao=13)
