"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

soma_idade = 0
homem_mais_velho = ''
mulher_menor_20 = 0
mais_velho = 0

for c in range(1, 5):
    print('-' * 5, '\033[34m{}ª PESSOA\033[m'.format(c), '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    soma_idade += idade

    if c == 1 and sexo == 'M':
        mais_velho = idade
        homem_mais_velho = nome
    if idade > mais_velho and sexo == 'M':
        mais_velho = idade
        homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulher_menor_20 += 1

print('A média de idade do grupo é {}.'.format(soma_idade/4))
print('O homem mais velho tem {} e se chama {}.'.format(mais_velho, homem_mais_velho))
print('Ao Todo são {} mulher(es) com menos de 20 anos.'.format(mulher_menor_20))
