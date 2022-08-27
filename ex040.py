'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

nota1 = float(input('Digite a primeira nota do aluno(a): '))
nota2 = float(input('Digite a segunda nota do aluno(a): '))
média = (nota1 + nota2) / 2
if média < 5:
    print('Com a nota {:.1f} e a nota {:.1f} o aluno está:'.format(nota1, nota2))
    print(média)
    print('REPROVADO!!')
elif 7 > média >= 5:
    print('Com a nota {:.1f} e a nota {:.1f} o aluno está:'.format(nota1, nota2))
    print(média)
    print('Recuperação')
elif média >= 7:
    print('Com a nota {:.1f} e a nota {:.1f} o aluno está:'.format(nota1, nota2))
    print(média)
    print('Aprovado!!')
