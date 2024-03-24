print('-='*23)
print('{:^46}'.format('SITUAÇÃO CADASTRAL DO ALUNO EXEMPLO 2'))
print('-='*23)
aluno = {}
aluno['nome'] = str(input('Aluno(a): '))
aluno['média'] = float(input(f'A Média do(a) {aluno["nome"]}: '))
if aluno['média'] >= 7.0:
    aluno['Situação'] = 'APROVADO!'
elif 5 <= aluno['média'] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO!'    
else:
    aluno['Situação'] = 'REPROVADO!'    
print('-='*23)  
for situacao, definida in aluno.items():
    print(f'{situacao}: {definida}')
print('-='*23)
  