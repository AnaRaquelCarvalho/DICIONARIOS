print('='*44)
print('{:^44}'.format(' APOSENTADORIA 2'))
print('='*44)
from datetime import date
dados = dict()
dados['nome'] = (str(input('NOME: '))).strip().title()
dados['nasc'] = (int(input('ANO DE NASCIMENTO: ')))
dados['ctps'] = (int(input('CARTEIRA DE TRABALHO Nº (0 Não tem): ')))
if dados['ctps'] != 0:
    dados['ctr'] = (int(input('ANO DE CONTRATAÇÃO: ')))
    dados['sal'] = (float(input('SALÁRIO R$: ')))
    apos = date.today().year - dados['ctr']
else:
    apos = -1
idade = date.today().year - dados['nasc']
print('=' * 44)
print(f'NOME DO USUÁRIO CADASTRADO: {dados["nome"]}')
print(f'IDADE DO USUÁRIO: {idade}')
if dados['ctps'] != 0:
    print(f'Carteira de Trabalho Nº {dados["ctps"]}')
    print(f'Salario R$ {dados["sal"]:.2f}')
    print(f'Data de contratação: {dados["ctr"]}')
    if apos > 35:
        print(f'A aposentadoria ja aconteceu !')
    else:
        print(f'TEMPO DE CONTRIBUIÇÃO: {apos} anos \nFALTA {35 - apos} anos para se aponsentar')
        print(f'IDADE DE APOSENTADORIA: {idade + (35 - apos)} anos de idade!')
else:
    print(f'Carteira de Trabalho: NÃO POSSUI')
print('='*44)    
