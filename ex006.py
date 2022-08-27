""" Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. """
n = int(input('Digite um número: '))
n1 = n + n
n2 = n * 3
n3 = n ** (1/2)
n4 = n ** (1/3)
#print('O dobro de {} vale {}'.format(n, n1))
#print('O triplo de {} vale {}'.format(n, n2))
#print('A raiz quadrada de {} é igual {:.2f}'.format(n, n3))
print('O dobro de {} vale {}.'.format(n,(n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))
print('A raiz cubica de {} é igual {:.2f}'.format(n, n4))
