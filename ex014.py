""" Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius
e converta para graus Fahrenheit. """
c = int(input('Digite a temperatura em °C: '))
f = 32 + (c * 9/5)
print('A sua temperatura em Fahrenheit é {:.1f}°F'.format(f))
