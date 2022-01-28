"""
Desafio 27
Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""

nome = str(input('Digite seu nome: ')).strip()
nome = nome.split()
aux = len(nome)
print('Primeiro: {}'.format(nome[0]))
print('Último  : {}'.format(nome[aux-1]))