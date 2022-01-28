"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

maior18 = 0
homem = 0
mulherMenor20 = 0
resposta = 'S'

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)

    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]

    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulherMenor20 += 1

    resposta = input('Deseja continuar? [S/N]').upper().strip()[0]
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N]').upper().strip()[0]

    if resposta == 'N':
        break

print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoa(s) com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homem} homen(s) cadastrados')
print(f'E temos {mulherMenor20} mulher(es) com menos de 20 anos')
