''' Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato. '''

total = p1k = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    barato = preco
    if preco < preco:
        barato = produto
    if preco >= 1000:
        p1k += 1
    total = total + preco
    escolha = str(input('Possui mais algum produto(s)? [S/N] ')).strip().upper()
    if escolha == 'N':
        break
print(f'Total da compra: R${total}\n{p1k} Produtos que custaram mais de R$1000.\nProduto mais barato: R${barato}')

