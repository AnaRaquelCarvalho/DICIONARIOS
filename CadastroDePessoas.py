print('='*30)
print('{:^30}'.format('CADASTRO DE PESSOAS'))
print('='*30)
Dados = dict()
cadastro = list()
soma = media = 0
while True:
    Dados.clear()
    Dados['nome'] = str(input("Nome: "))
    while True:
        Dados['Sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
        if Dados['Sexo'] in 'MF':
            break
        print('Opção Inválida! Responda apenas S ou N')
    Dados['idade'] = int(input("Idade: "))
    soma += Dados['idade'] 
    cadastro.append(Dados.copy())
    print('=' * 30)
    while True:
        resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        print('=' * 30)
        if resposta in 'SN':
           break
        print('Opção Inválida! Responda apenas S ou N')
    if resposta == 'N':
        break
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')   
media = soma / len(cadastro)
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram', end=' ')
for pes in cadastro:
    if pes['Sexo'] in 'Ff':
        print(f'{pes["nome"]} ',end= ' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for pes in cadastro:
    if pes['idade'] >= media:
        print('     ')
        for k, v in pes.items():
            print(f'{k} = {v}; ', end=' ')
        print()     
print('<<<< ENCERRADO >>>>')
print('=' * 30)


