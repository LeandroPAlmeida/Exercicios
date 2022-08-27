""" Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média """

pessoa = {}
human = []
media = soma = 0
while True:
    pessoa['nome'] = str(input('Digite seu nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Qual sua idade? '))
    soma += pessoa['idade']
    human.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input('Deseja adicionar outra pessoa? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('><' * 30)
print(f'A) Pessoas cadastradas: {len(human)}') #a
print('><' * 30)
media = soma / len(human) #b
print(f'B) A média de idade é de {media:5.2f} anos.')
print('><' * 30)
print('C) Mulheres cadastradas: ')
for p in human:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='') #c
print('><' * 30)
print(f'D) Pessoas acima da média de idade: ')
for p in human: #D
    if p["idade"] >= media:
        print(' ', end='')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
print()
print('><' * 30)
print('> FIM <')

