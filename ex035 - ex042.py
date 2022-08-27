'''Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo.'''

'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
# Verificação de quem é o menor
menor = r1
if r2 < r3 and r2 < r1:
    menor = r2
if r3 < r2 and r3 < r1:
    menor = r3
# Verificação de quem é o segundo menor
menor2 = r1
if r2 >= r3 and r2 <= r1:
    menor2 = r2
if r3 >= r2 and r3 <= r1:
    menor2 = r3
# Verificação de quem é maior
maior = r1
if r2 > r1 and r2 > r3:
    maior = r2
if r3 > r2 and r3 > r1:
    maior = r3
soma = menor + menor2
if soma > maior:
    print('Forma um triângulo!!')
    if menor == menor2 == maior:
       print('Mais especificamente um Equilátero!!')
    elif menor == menor2 or menor == maior:
       print('Mais especificamente um Isósceles!!')
    elif menor != menor2 and maior:
       print('Mais especificamente um Escaleno!!')
else:
    print('Não forma um triângulo!!')

