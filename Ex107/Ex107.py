""" Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções. """

import Moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${Moeda.metade(p)}')
print(f'O dobro de R${p} é R${Moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${Moeda.aumentar(p, 10)}')

