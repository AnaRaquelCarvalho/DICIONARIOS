print('='*55)
print('{:^55}'.format(' APOSENTADORIA 3'))
print('='*55)
from datetime import date
dados = {}
dados["Nome"] = str(input("Nome: ")).strip().title()
AnoNasc = int(input("Ano de Nascimento: "))
AnoAtual = date.today().year
dados["Idade"] = AnoAtual - AnoNasc 
dados["Carteira"] = int(input("Carteira de trabalho Nº (0 caso não tenha): "))
if dados["Carteira"] != 0:
    dados["Ano de contratação"] = int(input("Ano de contratação: "))
    dados["Salário"] = float(input("Salário R$ "))
    AnoAposentadoria = dados["Ano de contratação"] + 35
    IdadeAposentadoria = AnoAposentadoria - AnoNasc
    dados["Aposentadoria"] = IdadeAposentadoria
    print("="*55)
    print(f'''    - NOME: {dados["Nome"]}
    - IDADE: {dados["Idade"]}
    - CTPS: {dados["Carteira"]}
    - Ano de contratação: {dados["Ano de contratação"]}
    - Salário: R${dados["Salário"]}
    - Idade da aposentadoria: {dados["Aposentadoria"]}''')
else:
    print("="*55)
    print(f'''    - NOME: {dados["Nome"]}
    - IDADE: {dados["Idade"]}
    - CTPS: NÃO POSSUI!''')
print("="*55)    