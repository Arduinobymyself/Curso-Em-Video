

from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

cont = 0

while True:
    n = int(input('Diga um valor: '))
    resp = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while resp not in 'PI':
        resp = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    comp = randint(0, 10)

    result = 'PAR'
    soma = n + comp

    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'

    print('-' * 40)
    print(f'Você jogou {n} e o computador {comp}. Total de {soma} DEU {result}')
    print('-' * 40)

    if (resp == 'I' and result == 'ÍMPAR') or (resp == 'P' and result == 'PAR'):
        print('Você VENCEU!')
        cont += 1
    else:
        print('Você PERDEU!')
        break

print('=-' * 20)
print(f'GAME OVER! Você venceu {cont} vezes.')
