'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

n = t = 0
while True:
    n = int(input('Qual tabuada você deseja verificar: '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{c} x {n} = {c * n}')
