''' Exercício Python 114: Crie um código em Python que teste se o site
pudim está acessível pelo computador usado. '''

from socket import gethostbyname, create_connection

try:
    host = gethostbyname('www.pudim.com.br')
    s = create_connection((host, 80), 2)
    print('Consegui acessar o site Pudim com sucesso!')


except:
    print('O site Pudim não está acessível no momento!')
print(host.read())
