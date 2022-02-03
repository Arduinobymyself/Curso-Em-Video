'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
valores.sort()
print(f'Os valores digitados foram {valores}.')
for c in range(len(valores)):
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print('-=' * 30)
print(f'Os valores pares digitados foram: {pares}.')
print(f'Os valores impares digitados foram: {impares}.')