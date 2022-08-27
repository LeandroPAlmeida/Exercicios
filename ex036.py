""" Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. """

print('Vamos avaliar seu empréstimo!!')
vc = float(input('Qual o valor da casa/propriedade? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
pres = (vc / (anos * 12)) 
minimo = salário * 30 / 100
if pres <= minimo:
    print('Seu emprestimo foi aceito!!')
else:
    print('Seu emprestimo foi recusado!!')



