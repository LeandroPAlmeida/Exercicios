""" Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo. """
import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o Seno de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tangente))
