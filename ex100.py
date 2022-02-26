'''
Exercício Python 100: Faça um programa que tenha uma lista chamada números e
duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5
números e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint
from time import sleep

def sorteiaValores():
  print('-='*30)
  print('Sorteando 5 valores da lista: ', end='')
  valores = list()
  i = 1
  while i <= 5:
    valor = randint(0, 10)
    if valor not in valores:
      print(valor, end=' ', flush=True)
      sleep(.25)
      valores.append(valor)
      i += 1
  print('PRONTO!')
  return valores

def somaValoresPar(lista):
  soma = 0
  print(f'Somando os valores pares de {lista}, temos ', end='')
  for valor in lista:
    if valor % 2 == 0:
      soma += valor
  print(soma)



lista = sorteiaValores()
somaValoresPar(lista)
