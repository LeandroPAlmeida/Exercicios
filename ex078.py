''' Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

valores = list()
m = n = 0
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    if cont == 0:
        m = n = valores[cont]
    else:
        if valores[cont] > m:
            m = valores[cont]
        if valores[cont] < n:
            n = valores[cont]
print('-*' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior número digitado foi {m} na posições ', end='')
for i, v in enumerate(valores):
    if v == m:
        print(f'{i}º ... ', end='')
print()
print(f'O menor número digitado foi {n} na posições ', end='')
for i, v in enumerate(valores):
    if v == n:
        print(f'{i}º ... ', end='')
print()

