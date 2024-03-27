print('='*52)
print('{:^52}'.format('INFORMAÇÕES E  CADASTRO DE JOGADORES DE FUTEBOL '))
print('='*52)
cadastro = dict()
contador = list()
Dados = list()
from time import sleep
while True:
    cadastro.clear()
    cadastro['jogador'] = str(input(f"Nome do Jogador: ")).strip().title()
    partidas = int(input(f'Quantas partidas o {cadastro["jogador"]} jogou ? '))
    cadastro.clear()
    for c in range(0,partidas):
        contador.append(int(input(f'Quantos gols na {c+1}ª partida : ')))   
    cadastro['gols'] = contador[:]
    cadastro['total'] = sum(contador)
    Dados.append(cadastro.copy())
    print('='*52)
    while True:
        resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        print('='*52)
        if resposta in 'SN':
           break
        print('Opção Inválida! Responda apenas S ou N')
    if resposta == 'N':
        break
print(f'cod. nome        gols          total')
print('-'*36)
for pos, j in enumerate(Dados):
    
    

    