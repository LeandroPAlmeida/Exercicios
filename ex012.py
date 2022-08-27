""" Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. """
p = float(input('Digite o preço do produto: R$'))
dp = p - (p * 5/100)
print('Com o desconto de 5% sobre valor de R${:.2f}, você só irá pagar R${:.2f}'.format(p, dp))
