"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

t1 = int(input('Digite o 1° termo da progressão: '))
r = int(input('Digite a razão da progressão: '))

t10 = t1 + (10 - 1) * r

for c in range(t1, t10 + r, r):
    print('{} → '.format(c), end=' ')
print('Acabou!')