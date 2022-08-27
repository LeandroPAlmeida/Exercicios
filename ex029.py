""" Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite. """

velocidade = float(input('Digite sua velocidade: '))
if(velocidade > 80):
    multa = (velocidade - 80.0) * 7.00
    print('Você ultrapassou o limite permitido que é de 80 km/h e recebeu uma multa de: R${:.2f}'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Você não possui dispesas.')
    print('Tenha um bom dia! Dirija com segurança!')

