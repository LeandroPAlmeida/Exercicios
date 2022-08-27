""" Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu. """

'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''

from random import randrange
from time import sleep
n = int(input('Pensei num número de 0 a 5, qual você acha que foi!? '))
i = randrange(0, 10)
c = 0
while n != i:
    print('Processando...')
    sleep(1)
    n = int(input('Você errou, pensei em um número qual será? '))
    c += 1
    if n == i:
        print('Você acertou, pensei de fato no: {}'.format(i))
print('Você fez {} palpites até acertar!! '.format(c))

#Professor
from random import randint
computador = randint(0, 10)
print('Sou seu Computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas, Parabéns!'.format(palpites))
