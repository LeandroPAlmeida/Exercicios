""" Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva(‘Olá, Mundo!’) Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~
"""
def escreva(msg):
        t = len(msg) + 4
        print('-' * t)
        print(f'  {msg}')
        print('-' * t)


escreva(' Pablitow ')
