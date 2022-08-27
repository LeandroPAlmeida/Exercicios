'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. '''

mulhers = 0
soma = 0
média = 0
hmv = ''
for pessoa in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: \n[ M ] Masculino\n[ F ] Feminino\n')).strip()
    soma += idade
    if pessoa == 1 and sexo in 'Mm':
        hmv = nome
    if sexo in 'Mm':
        hmv = nome
    if sexo in 'Ff' and idade < 20:
            mulhers += 1
média = soma / 4
print('A média final de idade do grupo é {:.1f} meses.'.format(média))
print('O nome do homem mais velho é {}.'.format(hmv))
print('Total de mulheres com menos de 20 anos é {}.'.format(mulhers))