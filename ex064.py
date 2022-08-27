''' Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). '''

from time import sleep
n = 0
soma = 0
c = 0
while n <= 998:
    n = int(input('Digite um número: (Para parar o programa, digite "999") '))
    if n == 999:
        print('Finalizando...')
        sleep(1)
    else:
        soma = soma + n
        c += 1
print('A soma dos números {} digitados foi: {}.'.format(c, soma))

