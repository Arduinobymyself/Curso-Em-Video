"""
Desafio 25
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

#Entrada de dados
nome = input('Digite seu nome: ').strip().lower()

aux = nome.find('silva')
if aux > 0:
    print('Você é da Família "Silva"')
else:
    print('Você não é da Família "Silva"')