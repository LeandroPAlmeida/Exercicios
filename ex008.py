""" Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. """
m = int(input('Quantos metros você gostaria de converter? '))
print('{}m metro(s) medido(s) em centímetros é {:.0f}cm, e em milímetros é {:.0f}mm'.format(m, (m*100), (m*1000)))