print('='*52)
print('{:^52}'.format('INFORMAÇÕES E  CADASTRO DE JOGADORES DE FUTEBOL '))
print('='*52)
jogadores = list()
dados = dict()
gols = list()
while True:
    dados['Nome'] = input('\033[1;97mNome do(a) jogador(a): ').strip().title()
    partidas = int(input(f'Quantas patidas {dados["Nome"]} jogou? '))
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols marcou na {p+1}° partida? ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    jogadores.append(dados.copy())
    dados.clear()
    gols.clear()
    while True:
        continuar = input('\033[1;97mQuer continuar [S/N]? ').upper().strip()
        if continuar == 'S' or continuar == 'N':
            break
        print('\033[1;31mRESPOSTA INVÁLIDA!')
    print(60*'\033[1;97m-')
    if continuar == 'N':
        print('\033[1;32mJOGADORES CADASTRADOS'.center(60))
        c = 0
        for jogador in jogadores:
            c += 1
            espaco = 12 - len(jogador["Nome"])
            print(f'\033[1;97mN°{c}   Nome: {jogador["Nome"]}', end=espaco*' ')
            print(f'Gols: {jogador["Gols"]}', end=espaco*' ')
            print(f'Total: {jogador["Total"]}')
        break
while True:
    mostrar = int(input('\033[1;97mMostrar dados de qual jogador (digite 999 p/ encerrar)? '))
    if mostrar == 999:
        print('\033[1;33m==================>PROGRAMA ENCERRADO<======================')
        break
    elif mostrar > len(jogadores) or mostrar <= 0:
        print('\033[1;31mRESPOSTA INVÁLIDA!')
    else:
        print(60 * '\033[1;97m-')
        print('\033[1;34m ', end='')
        print(f'=====>LEVANTAMENTO DO JOGADOR(A) {jogadores[mostrar-1]["Nome"]}<====='.upper())
        for jogador in jogadores:
            if jogador == jogadores[mostrar-1]:
                for p, gol in enumerate(jogador['Gols']):
                    print(f'\033[1;97mNo {p + 1}° jogo fez {gol} gol(s)')
    print(60*'\033[1;97m-')
