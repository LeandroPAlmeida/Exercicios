''' Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. '''


from random import randint
n = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print(f'Os valores sorteados foram: {n}')
print(f'O maior valor sorteado foi o: N°{max(n)}.')
print(f'O menor valor sorteado foi o: N°{min(n)}.')
