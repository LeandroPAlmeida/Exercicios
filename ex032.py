""" Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto. """
ano = int(input('Digite o ano qualquer: '))
Bsexto = ano % 4
if Bsexto == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é Bissexto!'.format(ano))
