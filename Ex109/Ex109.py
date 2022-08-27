""" Exercício Python 109: Modifique as funções que foram criadas no desafio 107
para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser
ou não formatado pela função moeda(), desenvolvida no desafio 108. """

import Moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.metade(p, True)}')
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {Moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {Moeda.diminuir(p, 13, True)}')
