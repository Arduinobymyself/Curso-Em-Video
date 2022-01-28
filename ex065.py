"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

soma = media = cont = flag = 0
resp = 'S'

n = int(input('Digite um número: '))

maior = maior = n

while resp != 'N':
    cont += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    if resp == 'S':
        n = int(input('Digite um número: '))
media = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))



