'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

'''from datetime import date
yearnow = date.today().year
ano = int(input('Digite o seu ano de nascimento: '))
idade = yearnow - ano
if idade <= 9:
    print('Com base na sua idade, você será alocado na categoria MIRIM!!')
elif idade <= 14:
    print('Com base na sua idade, você será alocado na categoria INFANTIL!!')
elif idade <= 19:
    print('Com base na sua idade, você será alocado na categoria JÚNIOR!!')
elif idade <= 25:
    print('Com base na sua idade, você será alocado na categoria SÊNIOR!!')
else:
    print('Você será alocado na categoria MASTER!!')'''

#Professor
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

