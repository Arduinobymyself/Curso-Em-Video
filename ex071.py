"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 100
tot_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        tot_cedula += 1
    else:
        if tot_cedula > 0:
            print(f'total de {tot_cedula} cédulas de R${cedula} ')
        if cedula == 100:
            cedula = 50
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        tot_cedula = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
