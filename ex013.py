""" Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento. """
s = float(input('Digite seu salário: R$'))
ns = s + (s * 15/100)
print('Seu novo salário com aumento de 15% ficou R${}'.format(ns))