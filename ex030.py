""" Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. """
n = int(input('Digite um número inteiro: '))
n1 = n % 2
if n1 == 1:
    print('O número que você digitou é ímpar!')
else:
    print('O número que você digitou é par!')

