''' Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. '''
pessoas = []
dado = []
totmai = totmen = 0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite a peso: ')))
    if len(pessoas) == 0:
        totmai = totmen = dado[1]
    else:
        if dado[1] > totmai:
            totmai = dado[1]
        if dado[1] < totmen:
            totmen = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input('Deseja adicionar outra pessoa? [S/N] '))
    if resp in 'Nn':
        break
print(f'O total de pessoas cadastradas: {len(pessoas)}.')
print(f'Maior peso foi: {totmai}Kg dos cadastrados: ', end='')
for p in pessoas:
    if p[1] == totmai:
        print(f'[{p[0]}] ', end='')
print()
print(f'Menor peso foi: {totmen}Kg dos cadastrados: ', end='')
for p in pessoas:
    if p[1] == totmen:
        print(f'[{p[0]}] ', end='')
