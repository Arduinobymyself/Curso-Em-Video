"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.
"""

numeros = (int(input('Diigite um número: ')),
           int(input('Diigite outro número: ')),
           int(input('Diigite mais um número: ')),
           int(input('Diigite o último número: ')))

print(f'Você digitou os valores {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} vezez')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram ', end='')

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
