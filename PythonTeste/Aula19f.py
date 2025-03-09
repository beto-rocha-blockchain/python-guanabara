pessoas = {'nome': 'Beto', 'sexo': 'M', 'idade': 22}
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}') 
