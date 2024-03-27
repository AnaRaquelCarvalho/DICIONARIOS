print('='*60)
print('{:^60}'.format('CADASTRO DE JOGADORES DE FUTEBOL'))
print('='*60)
listadegols = []
listajogador = []
while True:
    soma = 0
    dadosjogador = {}
    dadosjogador['nome'] = str(input('NOME DO JOGADOR: '))
    dadosjogador['partidas'] = int(input(f"QUANTAS PARTIDAS {dadosjogador['nome']} jogou: "))
    for c in range(0, dadosjogador['partidas']):
        golos = int(input(f'QUANTOS GOLS FORAM FEITOS NA {c + 1})° PARTIDA: '))
        listadegols.append(golos)
    dadosjogador['gols'] = listadegols[:]
    soma = sum(listadegols)
    dadosjogador['totaldegols'] = soma
    listajogador.append(dadosjogador)
    listadegols.clear()
    resp = str(input('quer continuar [S/N]: ')).upper()
    if resp in 'Nn':
        break
print('-=' * 45)
print(f'{"Cod":<5} {"nome":<15} {"gols":<14} {"total":>7}')
print('-=' * 45)
for c, jogador in enumerate(listajogador):
    print(f'{c:<5} {jogador["nome"]:<15} {", ".join(map(str,jogador["gols"])):<14} {jogador["totaldegols"]:>7}')
print('-=' * 45)
while True:
    while True:
        dada = int(input('Mostra dados de qual jogador [999 para não mostrar nenhum]? '))
        if dada > len(listajogador) - 1 and dada != 999:
            print(f'ERRO! Não existe jogador com código {dada}! Tente Novamente')
            print('-' * 45)
        else:
            break
    if dada <= len(listajogador) - 1:
        print(f'--- Levantamento do jogador {listajogador[dada]["nome"]}')
        for c in range(0, len(listajogador[dada]["gols"])):
            print(f'No jogo {c + 1} fez {listajogador[dada]["gols"][c]} gols')
        print('-' * 45)
    if dada == 999:
        break
