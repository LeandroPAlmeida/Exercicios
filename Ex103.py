""" Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
 O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente. """

def ficha(nome = 'desconhecido', gols = 0):
    print(f'O Jogador {nome} marcou um total de {gols} Gol(s) no campeonato.')


#Programa Principal
n = str(input('Nome do jogador: '))
g = str(input(f'Quantos gol(s) {n} marcou: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    print(ficha(n, g))
