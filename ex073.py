''' Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense. '''

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Bragantino', 'Corinthians', 'Fortaleza', 'Internacional', 'América-MG', 'Fluminense', 'Athletico-PR', 'Santos', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'São Paulo', 'Bahia', 'Juventude', 'Sport Recife', 'Grêmio', 'Chapecoense')
print('-_-'*20)
print(f'Lista de times do Brasileirão: {times}')
print('-_-'*20)
print(f'Os 5 primeiros times são: {times[:5]}')
print('-_-'*20)
print(f'Os 4 últimos são: {times[16:21]}')
print('-_-'*20)
alfa = (sorted(times))
print(f'Times em ordem alfábética: {alfa}')
print('-_-'*20)
chape = times.index('Chapecoense') + 1
print(f'O time Chapecoense está na {chape}° posição!')
