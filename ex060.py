"""
Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
"""
'''
from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print('Calculando {}! = {}'.format(n, f))
'''


n = int(input('Digite um número: '))
cont = n
f = 1

print('Calculando {}!: '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')

    f *= cont
    cont -= 1
print('{}'.format(f))







