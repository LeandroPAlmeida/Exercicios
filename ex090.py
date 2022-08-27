""" Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.No final, mostre o conteúdo da estrutura na tela. """
nome = str(input('Digite seu nome: '))
média = float(input('Média: '))
if média >= 7:
    situacao = 'Aprovado'
elif 5 <= média < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'
aluno = {nome, média, situacao}
print(f'Nome: {nome} | Média: {média} | Situação: {situacao}')
