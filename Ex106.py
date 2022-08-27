""" Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores. """

from time import sleep
c = ('\033[m',           # 0 - Sem cores
     '\033[0;30;41m',    # 1 - Vemelho
     '\033[0;30;42m',    # 2 - Verde
     '\033[0;30;43m',    # 3 - Amarelo
     '\033[0;30;44m',    # 4 - Azul
     '\033[0;30;45m',    # 5 - Roxo
     '\033[0;30m'        # 6 - Branco
     );


def save(n):
    título(f'Acessando o manual do comando \'{n}\'', 4)
    print(c[5], end='')
    help(n)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('*' * tam)
    print(f'  {msg}')
    print('*' * tam)
    print(c[0], end='')
    sleep(1)


#Programa Principal
resp = ''
while True:
    título('Sistema de Ajuda PyHelp', 2)
    resp = str(input('\033[31;40mFunção ou Biblioteca: '))
    if resp == 'fim':
        break
    else:
        save(resp)
título('Até logo!', 1)

