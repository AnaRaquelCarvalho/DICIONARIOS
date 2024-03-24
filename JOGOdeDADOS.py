print('-='*23)
print('{:^46}'.format(' JOGO DE DADOS - OBSERVAÇÃO -> COM NOVAS FUNÇOES '))
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'JOGADOR MARINO ': randint(1,6),
        'JOGADOR EDUARDO ': randint(1,6), 
        'JOGADOR AMANDA ': randint(1,6), 
        'JOGADOR JOANA ': randint(1,6)}
print(' ')
ranking = list()
print('-='*7,' VALORES SORTEADOS ','-='*7)
for jogador, dados in jogo.items():
    sleep(1)
    print(f'O {jogador}, Jogou O Dado e tirou  no {dados} dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(' ')  
print('-='*5, ' RANKING DOS JOGADORES ','-='*5)
for cont, vencedor in enumerate(ranking):
    sleep(1)
    print(f'{cont+1}º LUGAR {vencedor[0]} >> com {vencedor[1]} no PONTOS no DADO.')
print('-='*23)
