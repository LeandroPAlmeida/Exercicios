''' Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. '''

num = []
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Deseja adicionar mais algum número? [S/N] '))
    if r in 'Nn':
        break
print(f'A) {len(num)} digitados.')
num.sort(reverse=True)
print(f'B) {num}.')
if 5 in num:
    print(f'C) O valor 5 está na lista.')
else:
    print(f'C) O valor 5 não está na lista.')

