'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter

# sorteia os valores e armazenas nas keys de um dictionary
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)
        }

ranking = list()

print('Valores Sorteados:')
for k, v in jogo.items():
  print(f'{k} tirou {v} no dado')
  sleep(1)

# classifica por item de forma reversa
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

#print(ranking) # o resultado está em uma forma de: lista de tuplas

print('-='*30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
  print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
  sleep(1)

