'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.

Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

#Ex51
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for c in range(1, 11):
    pa = t + (c - 1) * r
    print('A progressão aritmética do {}° termo {} e a razão {} é: {}'.format(c, t, r, pa))

#Ex61
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
while c < 10:
    pa = t + (c - 1) * r
    c += 1
    print("A progressão aritmética do {}° termo {} e a razão {} é: {}.".format(c, t, r, pa))

#Ex62
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
termos = 0
tm = 10
while tm != 0:
    while c <= termos:
        print('{} -> '.format(t), end='')
        t += 1
        c += 1
    mais = int((input('Quantos termos você quer mostrar a mais? ')))
    termos = termos + mais
    if mais == 0:
        tm = 0
print('Progressão finalizada com {} termos mostrados!'.format(termos))



