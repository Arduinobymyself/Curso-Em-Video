"""
Desafio 24
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""

#entrada de dados
cidade = input('Digite o nome da Cidade:')

#Calculos
cidade = cidade.lower().strip().split()
aux = cidade[0] == 'santo' or cidade[0] == 'são'

#Saída de dados
if aux:
    print('O nome da Cidade começa com "Santo" ou "São"')
else:
    print('O Nome da Cidade não começa com "Santo" ou "São"')