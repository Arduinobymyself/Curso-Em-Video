'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que
analisar todos os valores e dizer qual deles é o maior.
'''

from time import sleep

def analisaValores(*valores):
  print('-='*30)
  print('Analisando valores passados...')
  cont = maior = 0
  for valor in valores:
    cont += 1
    print(valor, end=' ', flush=True)
    sleep(.25)
    if valor > maior:
      maior = valor
  print(f'Foram informados {cont} valores ao todo.')
  print(f'O maior valor informado foi {maior}')




analisaValores(2, 9, 4, 5, 7, 1, 20, 31, 6, 52)
analisaValores(4, 7, 0)
analisaValores(1, 2)
analisaValores(6)
analisaValores()
