"""
Crie um programa que tenha uma dupla totalmente preenchida com
uma contagem por extenso, de zero até vinte. Seu programa
deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oite',
           'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoite', 'Dezenove', 'Vinte')

while True:
    n = int(input('Tente novamente. Digite um número entre 0 e 20:'))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')

print(f'Você digitou o número {numeros[n]}')
