""" Exercício Python 100: Faça um programa que tenha uma lista chamada números e
duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior. """

from random import randint
números = []
def sorteia(lst):
    for c in range(0, 5):
        n = randint(0, 100)
        números.append(n)
    print(f'Números sorteados: {lst}.')


def somaPar(lst):
    soma = 0
    for v in números:
        if v % 2 == 0:
            soma += v
    print(f'O total da soma dos números pares é de {soma}.')


sorteia(números)
somaPar(números)
