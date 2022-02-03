'''
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''

valores = [[], []]  # valores[0] para os pares e valores[1] para os ímpares
for i in range(0, 7):
    n = int(input(f'Digite o {i+1}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)  # se par
    else:
        valores[1].append(n) # se ímpar
valores[0].sort()
valores[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores impares digitados foram: {valores[1]}')
