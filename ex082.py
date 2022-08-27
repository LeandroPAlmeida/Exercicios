''' Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas. '''

num = []
par = []
imp = []
while True:
    v = (int(input('Digite um número: ')))
    if v % 2 == 0:
        num.append(v)
        par.append(v)
    else:
        num.append(v)
        imp.append(v)
    resp = str(input('Deseja adicionar outro número: [S/N] '))
    if resp in 'Nn':
        break
print(f'Todos os números adicionados: {num}.')
print(f'Pares: {par}.')
print(f'Ímpares: {imp}.')















