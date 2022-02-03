'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

# define a matriz 3 x 3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = 0
somaCol3 = 0
maiorLinha2 = matriz[1][0]

# preenche a matriz 3 x 3 com dados entrados pelo usuário
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite o valor para [{l}][{c}]: ')))
        # se par, soma
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        # se coluna 3, soma
        if c == 2:
            somaCol3 += matriz[l][c]
        #se linha 2, toma o maior
        if l == 1:
            if matriz[l][c] > maiorLinha2:
                maiorLinha2 = matriz[l][c]

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
     print(f'[{matriz[l][c]:^4}]', end='')
    print()
print('-=' * 30)

print(f'A soma dos valores pares é: {somaPar}')
print(f'A soma dos valores da terceira coluna é: {somaCol3}')
print(f'O maior valor da segunda linha é: {maiorLinha2}')
print('-=' * 30)
