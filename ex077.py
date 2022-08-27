'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

Mercado = 'Uva', 'Laranja', 'Pera'
for c in Mercado:
    print(f'\nNa palavra {c.upper()} são', end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')



