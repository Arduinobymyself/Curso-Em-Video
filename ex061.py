"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a estrutura while.
"""
t1 = int(input('[t1] 1° termo da progressão: '))
r = int(input('[r] razão da progressão: '))
n = int(input('[n] Quantos termos: ')) # melhoria adiciona sem ser solicitada

termo = t1
cont = 1

while cont <= n:
    print('{} → '.format(termo), end=' ')
    termo += r
    cont += 1
print('Fim')


