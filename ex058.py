"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
"""

import random
from random import randint

print('Sou seu computador...')
computador = randint(0,10)
print('Acabei de pensar em número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')

acertou = False
tentativas = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1

    if computador == jogador:
       acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        else:
            print('Menos... tente mais uma vez')

print('Acertou na {}ª tentativa. Parabéns!'.format(tentativas))




