''' Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). '''

n = int(input('Digite um número inteiro ou para encerrar digite 999: '))
s = c = 0
while n < 999:
    s = s + n
    c += 1
    n = int(input('Digite um número inteito ou para encerrar digite 999: '))
    if n >= 999:
        break
print(f'Total de números digitados {c}, com a soma de {s}.')

