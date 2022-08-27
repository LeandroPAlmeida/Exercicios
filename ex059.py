'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

entrada = 0
while entrada != 5:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    entrada = int(input('O que deseja fazer com os valores: \n[ 1 ] Somar\n[ 2 ] Multplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n'))
    if entrada == 1:
        soma = n1 + n2
        print('O valor da soma foi: {}.'.format(soma))
    elif entrada == 2:
        mult = n1 * n2
        print('O resultado da multiplicação foi: {}.'.format(mult))
    elif entrada == 3:
        if n1 > n2:
            maior = n1
            print('O número maior digitado foi: {}.'.format(maior))
        else:
            maior = n2
            print('O maior número digitado foi: {}.'.format(maior))
    elif entrada == 4:
        print('Digite os novos valores:')
    elif entrada == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('Volte quando quiser!!')
