""" Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você. """
from random import randint
print('{:=^50}'.format(' Bem vindo(a)'))
escolha = ('Pedra', 'Papel', 'Tesoura')
ia = randint(0, 2)
jogador = int(input('Vamos jogar Jokenpô!! Escolha uma opção: \n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura\n'))
if jogador == 1 and ia == 2:
    print('Parabéns, você me venceu. Escolhi {}.!!'.format(escolha[ia]))
elif jogador == 1 and ia == 1:
    print('Você perdeu, escolhi {}.!!'.format(escolha[ia]))
elif jogador == 1 and ia == 0:
    print('Empatamos, também escolhi {}.!!'.format(escolha[ia]))
elif jogador == 2 and ia == 2:
    print('Você perdeu, escolhi {}.'.format(escolha[ia]))
elif jogador == 2 and ia == 1:
    print('Empatamos, também escolhi {}.'.format(escolha[ia]))
elif jogador == 2 and ia == 0:
    print('Parabéns, Você ganhou. Escolhi {}.'.format(escolha[ia]))
elif jogador == 3 and ia == 2:
    print('Empatamos, também escolhi {}.'.format(escolha[ia]))
elif jogador == 3 and ia == 1:
    print('Parabéns, Você ganhou. Escolhi {}.'.format(escolha[ia]))
elif jogador == 3 and ia == 0:
    print('Você perdeu, Escolhi {}.'.format(escolha[ia]))
else:
    print('Entrada Inválida!!')
