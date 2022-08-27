""" Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. """
a = float(input('Qual a altura: '))
l = float(input('Qual a largura: '))
area = a * l
print('Com {}m² de área, você irá precisar de {}L para realizar a pintura completa.'.format(area, (area/2)))