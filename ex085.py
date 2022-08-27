''' Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente. '''

n = []
par = []
impar = []
for c in range(1, 8):
    num = int(input(f'Digite o {c} número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
print(f'Os números pares digitados foram: {par}.')
print(f'Os números ímpares digitados foram: {impar}.')
n.append(par[:])
n.append(impar[:])
par.clear()
impar.clear()















