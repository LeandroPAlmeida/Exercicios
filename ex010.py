""" Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. """
c = float(input('Quanto você quer converter: R$'))
print('Com R${:.2f} você terá, US${:.2f} em doláres'.format(c, (c * 3.27)))


