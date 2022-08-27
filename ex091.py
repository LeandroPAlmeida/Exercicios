""" Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""
from random import randint
from time import sleep
from operator import itemgetter
rank = ()
jogadores = {'jogador 1': randint(1, 6),
             'jogador 2': randint(1, 6),
             'jogador 3': randint(1, 6),
             'jogador 4': randint(1, 6)}
for a, b in jogadores.items():
    print(f'--> {a} tirou {b} ')
    sleep(1)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Rank dos Jogadores!!')
for i, v in enumerate(rank):
    print(f'{i+1}o lugar: {v[0]} com {v[1]}')
    sleep(1)