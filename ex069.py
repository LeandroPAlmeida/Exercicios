''' Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos. '''

maior = homens = mulheres20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [F/M] ')).strip().upper()[0]
    while sexo not in 'MF':
       sexo = str(input('Digite seu sexo: [F/M] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    escolha = str(input('Quer adicionar mais alguma pessoa? [S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Quer adicionar mais alguma pessoa? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'Das pessoas cadastradas {maior} já são maiores de 18 anos, sendo que {homens} homens foram cadastrados e {mulheres20} mulheres com menos de 20 anos.')