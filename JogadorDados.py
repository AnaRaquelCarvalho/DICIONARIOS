print('='*60)
print('{:^60}'.format('CADASTRO DE JOGADORES DE FUTEBOL'))
print('='*60)
cadastro = dict()
contador = list()
cadastro['jogador'] = str(input(f'Nome do Jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas o {cadastro["jogador"]} jogou ? '))
for c in range(0,partidas):
    contador.append(int(input(f'Quantos gols na {c+1}ª partida : ')))
print('='*60)
cadastro['gols'] = contador[:]
cadastro['total'] = sum(contador)
print('='*60) 
print(f'==> O jogador {cadastro["jogador"]} jogou {partidas} partidas.')
for cont, jogos in enumerate(contador):
    print(f'==> Na {cont+1}ª partida, fez {jogos} gols.')   
print(f'==> {sum(contador)} Gols no TOTAL.')
print('='*60)