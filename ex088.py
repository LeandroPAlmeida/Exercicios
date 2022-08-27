''' Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta. '''

from random import randint
from time import sleep
game = []
lista = list()
resp = int(input('Quantos jogos você deseja: '))
a = 1
while a <= resp:
    i = 0
    while True:
        num = randint(1, 60)
        if num not in game:
            lista.append(num)
            i += 1
        if i >= 6:
            break
    lista.sort()
    game.append(lista[:])
    lista.clear()
    a += 1
print(f'Sorteando {resp} jogos')
for i, v in enumerate(game):
    print(f'Jogo {i+1}: {v}')
    sleep(1)
