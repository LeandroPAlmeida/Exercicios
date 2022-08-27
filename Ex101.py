""" Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições. """
from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        print(f'Com {idade}  anos: Não é preciso votar!!')
    if idade >= 18 and idade < 65:
        print(f'Com {idade} anos: Seu voto é obrigatório!!')
    if idade >= 65:
        print(f'Com {idade} anos: Seu voto é opcional!!')


ano = int(input('Digite seu ano de nascimento: '))
voto(ano)
