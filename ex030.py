"""
Crie um programa que leia um número e
mostre na tela se ele é PAR ou IMPAR.
"""
n = int(input('Digite um número qualquer: '))
if n%2 == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é IMPAR.'.format(n))
