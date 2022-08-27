""" Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. """
qt = int(input('Por quantos dias você alugou o veiculo? '))
km = float(input('Quantos Km rodados: '))
pagar = (qt * 60) + (km * 0.15)
#rodado = km * 0.15
print('Valor total a pagar: R${:.2f}'.format(pagar))
