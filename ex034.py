""" Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%. """
salário = float(input('Digite seu salário: '))
if salário >= 1250:
    aumento = (salário * 10 / 100) + salário
    print('Você teve um aumento de 10%, seu salário agora é: R${:.2f}.'.format(aumento))
else:
    aumento = (salário * 15 / 100) + salário
    print('Você teve um aumento de 15%, seu salário agora é: R${:.2f}.'.format(aumento))


