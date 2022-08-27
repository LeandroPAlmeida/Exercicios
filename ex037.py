""" Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal. """

n = int(input('Digite um número inteiro: '))
opção = int(input('Digite a conversão desejada: \n[1] Binário \n[2] Octal \n[3] Hexadecimal\n'))

if opção == 1:
    print('O valor {} em binário é {}.'.format(n, bin(n)[2:]))
elif opção == 2:
    print('O valor {} em octal é {}.'.format(n, oct(n)[2:]))
elif opção == 3:
    print('O valor {} em hexadecimal é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente!!')


