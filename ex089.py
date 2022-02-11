'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.
'''

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break

print('-=' * 30)
print(f'{"nº":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)

for i, a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar as notas de qual aluno? (0 para sair): '))
    if opc == 0:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc-1][0]} são {ficha[opc-1][1]}')

print('VOLTE SEMPRE!')

