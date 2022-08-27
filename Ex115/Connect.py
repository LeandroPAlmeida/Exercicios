def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarAquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[0;31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def cadastro(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[0;31mHouve um ERRO na abertura do aquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[0;31mHouve um ERRO na hora de escrever os dados!\033[m')


def lerAquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[0;31mERRO ao ler o arquivo!\033[m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()

