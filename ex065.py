''' Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. '''

verif = 'S'
maior = menor = média = c = 0
while verif in 'Ss':
    n = int(input('Digite um número: '))
    média += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    verif = str(input('Deseja adicionar mais números? [S/N] ')).upper().strip()[0]
média = média / c
print('Com base nos números digitados, o número maior foi {} e o menor {}, com média de {:.1f}.'.format(maior, menor, média))
