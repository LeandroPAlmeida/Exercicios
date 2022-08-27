''' Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um número inteiro para ver a tabuada: '))
print('A tabuada do número inteiro {} é: ')
print('-'*12)
print(n*1)
print(n*2)
print(n*3)
print(n*4)
print(n*5)
print(n*6)
print(n*7)
print(n*8)
print(n*9)
print(n*10)
print('-'*12)'''

'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''
n = int(input('Digite um número inteiro para ver a tabuada: '))
print('A tabuada do número inteiro {} é: '.format(n))
print('-'*12)
for c in range(0, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
print('-'*12)


