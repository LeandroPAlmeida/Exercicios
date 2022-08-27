from time import sleep
from Exercicios.Ex115.Connect import *

#Programa Prinicpal
arq = 'Pessoa.txt'

if not arquivoExiste(arq):
    criarAquivo(arq)

while True:
    print('*' * 30)
    print(f'Menu Principal'.center(30))
    print('*' * 30)
    print('1 - Ver pessoas cadastradas', '\n2 - Cadastrar uma pessoa', '\n3 - Sair do sistema')
    print('*' * 30)
    resp = int(input('Digite a opção desejada: '))
    if resp == 1:
        lerAquivo(arq)
        sleep(0.3)
    elif resp == 2:
        nome = str(input('Digite seu nome: ')).strip()
        idade = int(input('Digite sua idade: '))
        cadastro(arq, nome, idade)
        sleep(0.3)
        print(f'Casdastro de(a) {nome} efetuado com sucesso!')
    elif resp == 3:
        sleep(0.1)
        print('Obrigado pela preferência, até logo.')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
        sleep(0.2)

