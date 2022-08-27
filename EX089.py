""" Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente. """

lista = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], média])
    resp = str(input('Deseja adicionar outro aluno? [S/N] '))
    if resp in 'Nn':
        break
print(f'{"No.":<5}{"Nome":<7}{"Média":>4}')
print('-=' * 28)
for i, a in enumerate(lista):
    print(f'{i:<5}{a[0]:<7}{a[2]:>4.1f}')
while True:
    print('-=' * 30)
    resp1 = int(input('Gostaria de ver as notas de algum aluno? (999 encerra o programa!!) '))
    if resp1 == 999:
        break
    if resp1 <= len(lista):
        print(f'Notas de {lista[resp1][0]} são {lista[resp1][1]}')
print('Finalizando...')
