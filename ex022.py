"""
desafio 22
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras Maiúsculas.
O nome com todos as letras miúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.
"""
#Entrada de dados
nome = input('Digite seu nome completo: ')

#saídas
print('Seu mone em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem: {} letras.'.format((len(nome)-nome.count(' '))))
nome = nome.split()
print('Seu primeiro nome é: {} e tem {} letras.'.format(nome[0], len(nome[0])))