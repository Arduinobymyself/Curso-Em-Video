'''
Crie um programa que declare uma matriz de dimensão 3×3
e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela, com a formatação correta.
'''

# define a matriz 3 x 3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# preenche a matriz 3 x 3 com dados entrados pelo usuário
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite o valor para [{l}][{c}]: ')))

# resultados
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
     print(f'[{matriz[l][c]:^4}]', end='')
    print()
