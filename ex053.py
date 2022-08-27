''' Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA. '''

frase = str(input('Me diga uma frase: ')).strip().upper()
fsplit = frase.split()
fjoin = ''.join(fsplit)
inverso = ''
for letras in range(len(fjoin) -1, -1, -1):
    inverso += fjoin[letras]
print('A frase digitada ao contrário ficou: {}.'.format(inverso))
if fjoin == inverso:
    print('A frase {} é um políndromo!!'.format(frase))
else:
    print('A frase digitada não é um políndromo!!')




