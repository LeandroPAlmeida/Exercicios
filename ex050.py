'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

s = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    calc = n % 2
    if calc == 0:
        s += n
print('A soma dos números inseridos foi {}.'.format(s))

