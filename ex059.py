"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

op = 0

while op != 5:

    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')

    op = int(input('>>>> Qual opção? '))

    if op == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 == n2:
            print(' {} e {} são iguais'.format(n1, n2))
        elif n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
    elif op == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    elif op == 5:
        pass
    else:
        print('Opção Inválida. Tente novamente')
    print('~*~~' * 10)
    sleep(2)

print('Fim do programa! Volte sempre!')








