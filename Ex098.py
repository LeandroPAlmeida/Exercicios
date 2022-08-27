""" Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada """
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i}, até {f} de {p} em {p}.')
    sleep(0.5)
    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c += p
        print('Fim')
    else:
        c = i
        while c >= f:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c -= p
        print('Fim')
print('><' * 29)


#Programa Pricipal
print('Contador')
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Digite o ínicio da contagem: '))
fim = int(input('Digite o fim da contagem: '))
passo = int(input('Digite quantas casas deseja pular: '))
contador(inicio, fim, passo)
