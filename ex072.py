''' Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. '''

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    resp = int(input('Digite um número entre 0 e 20: '))
    if 0 <= resp <= 20:
        print(f'Você digitou o número {n[resp]}.')
        escolha = str(input('Deseja ver outro número? [S/N] ')).strip().lower()[0]
        if escolha in 'Ss':
            continue
        if escolha in 'Nn':
            print('O programa foi encerrado!')
            break
