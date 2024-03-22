print('-='*23)
print('{:^46}'.format(' EXEMPLO DE DICIONÁRIO'))
print('-='*23)
estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['UF'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
