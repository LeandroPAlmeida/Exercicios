''' Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e
preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.

Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. '''

raiz = [[], [], []]
par = terceira = maior = 0
for v in range(0, 9):
    c = int(input('Qual número deseja adicionar a raiz 3x3? '))
    if c % 2 == 0:
        par = par + c
    if v < 3:
        raiz[0].append(c)
    elif v >= 3 and v <= 5:
        raiz[1].append(c)
    else:
        raiz[2].append(c)
terceira = raiz[0][2] + raiz[1][2] + raiz[2][2]
if raiz[1][0] >= raiz[1][1] and raiz[1][0] >= raiz[1][2]:
    maior = raiz[1][0]
elif raiz[1][1] >= raiz[1][2] and raiz[1][1] >= raiz[1][0]:
    maior = raiz[1][1]
else:
    maior = raiz[1][2]
print(f'{raiz[0]}')
print(f'{raiz[1]}')
print(f'{raiz[2]}')

print('Ex087')
print(f'A soma de todos os valores pares é: {par}.')
print(f'A soma dos valores da terceira coluna é: {terceira}.')
print(f'O maior valor da segunda linha é: {maior}.')






