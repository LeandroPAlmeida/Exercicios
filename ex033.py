""" Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor. """
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
lista = [n3, n2, n1]
lista0 = sorted(lista)
print('O maior entre os 3 números digitados é {} e o menor é o {}.'.format(lista0[2], lista0[0]))

