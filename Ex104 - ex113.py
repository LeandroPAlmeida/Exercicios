""" Exercício Python 104: Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante á função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)

Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade. """


def leiaInt(msg):
    while True:
        try:
           n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por Favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO: Por Favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


#Programa Principal
num = leiaInt('Digite um número inteiro: ')
print(f'O valor digitado: {num}')
num = leiaFloat('Digite um número real: ')
print(f'O valor digitado: {num}')
