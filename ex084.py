'''
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

galera = list()
pessoa = list()
maiorPeso = 0
menorPeso = 0
while True:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input('Peso: ')))
    if len(galera) == 0:
        maiorPeso = menorPeso = pessoa[1]
    else:
        if pessoa[1] > maiorPeso:
            maiorPeso = pessoa[1]
        if pessoa[1] < menorPeso:
            menorPeso = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {maiorPeso} Kg. Peso de: ', end='')
for p in galera:
    if p[1] == maiorPeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorPeso} Kg. Peso de: ', end='')
for p in galera:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end='')




