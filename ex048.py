"""
Faça um programa que calcule a soma entre todos os números que são
múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
soma = 0
contador = 0
for c in range(1, 501):
    if not (c % 2 == 0):#se for par não interessa!
        if c % 3 == 0:#não é par!, é divisível por 3?
            contador += 1
            soma += c
print('A soma dos {} valores solicitados é {}'.format(contador, soma))
print('Que são todos os ímpares múltiplos de 3 no range de 1 a 500')


"""
Resolução CEV
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
print('A soma dos {} valores solicitados é {}'.format(contador, soma))
print('Que são todos os ímpares múltiplos de 3 no range de 1 a 500')
"""