""" Exercício Python 092: Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. """

from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Digite seu nome: '))
nasc = int(input('Digite sue ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['carteira'] = int(input('Possui carteira de trabalho? (0 para não tem) '))
if pessoa['carteira'] != 0:
    pessoa['CTPS'] = int(input('Em qual ano foi contratado? '))
    pessoa['salario'] = float(input('Qual seu salário? R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['CTPS'] + 35) - datetime.now().year)
print('><' * 30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')












