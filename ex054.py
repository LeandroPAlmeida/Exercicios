''' Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. '''

from datetime import date
today = date.today().year
menor = 0
maior = 0
for c in range(0, 7):
    pessoa = int(input('Digite o ano do seu nascimento: '))
    idade = today - pessoa
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas das sete que participaram não atingiram a maior idade e {} já são maiores.'.format(menor, maior))
