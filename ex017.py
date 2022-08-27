""" Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa. """
#1° Jeito (sem import!!)
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# 2° Jeito
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
