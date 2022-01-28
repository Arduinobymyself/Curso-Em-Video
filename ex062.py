"""
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

t1 = int(input('[t1] 1° termo da progressão: '))
r = int(input('[r] razão da progressão: '))

termo = t1
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end=' ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você quer mostrar? '))
print('Progressão finalizada, {} termos mostrados'.format(total))
