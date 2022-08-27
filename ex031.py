""" Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas. """
distância = int(input('Digite a distância da sua viagem em Km: '))
if distância <= 200:
    custo = distância * 0.50
    print('Com base na distância digitada, sua viagem custará: R${:.2f}.'.format(custo))
else:
    cust = distância * 0.45
    print('Com base na distância digitada, sua viagem custará: R${:.2f}.'.format(cust))

