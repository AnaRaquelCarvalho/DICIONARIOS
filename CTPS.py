print('-='*16)
print('{:^36}'.format(' APOSENTADORIA'))
print('-='*16)
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho: (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*16)
for apos, valor in dados.items():
    print(f' >>> {apos} tem o valor {valor}')
print('-='*16)    
    





    