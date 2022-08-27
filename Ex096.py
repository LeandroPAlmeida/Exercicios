""" Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno. """

def área(comprimento, largura):
    area = comprimento * largura
    print(f'A área do seu terreno é de {area}m².')


print('Bem vindo: A descubra a área!!')
print('><' * 29)
comprimento = float(input('Digite o comprimento do terreno em (m): '))
largura = float(input('Digite a largura do terreno em (m): '))
área(comprimento, largura)
