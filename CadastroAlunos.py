print('-='*23)
print('{:^46}'.format('SITUAÇÃO CADASTRAL DO ALUNO'))
print('-='*23)
aluno = {'nome': str(input('Nome: '))}
aluno['Média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['Média'] >= 7:
	aluno['Situação'] = 'Aprovado!' 
if 5 < aluno['Média'] <7: 
	aluno['Situação'] = 'Recuperação!'
else:
	aluno['Situação'] = 'Reprovado' 
print('-='* 7,' RESULTADO FINAL ','-='*7)	
for situacao, resultado in aluno.items():
	print(f'{situacao}:', resultado)
print('-='*23)	
	
	