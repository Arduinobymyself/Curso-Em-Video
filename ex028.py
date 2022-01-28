"""
Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 a 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu
"""

#from random import choice
#lista = [0, 1, 2, 3, 4, 5]
#nc = choice(lista)
from random import randint
from time import sleep

nc = randint(0, 5)
print('-=-'*20)
print('Vou "pensar" em um número entre 0 e 5. Tente Advinhar!')
print('-=-'*20)
print('Processando...\n')
sleep(3)
nh = int(input('Em que número pensei? '))

if nh == nc:
    print('\nPARABÉNS!, você conseguiu me vencer!')
else:
    print('\nLamento, você ERROU!')
    print('Eu "pensei no número {} e não no {}'.format(nc, nh))
