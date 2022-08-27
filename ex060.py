''' Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120 '''

from math import factorial
número = int(input('Digite um número para efetuar seu fatorial: '))
calculo = factorial(número)
print('O fatorial de {} é {}.'.format(número, calculo))

