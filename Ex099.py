""" Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior. """

def maior(*num):
    mai = c = 0
    for c in range(0, len(num)):
        if c == 0:
            mai = num[c]
        if num[c] >= mai:
            mai = num[c]
    print(f'O maior valor informado foi {mai}.')


#Programa Principal
maior(2, 4, 85)
maior(0, 5, 8, 28)
maior()
