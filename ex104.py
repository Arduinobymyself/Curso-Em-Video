'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)
'''


def leiaInt(mensagem):
    flag = False
    n = 0
    while True:
        n = str(input(mensagem)).strip()
        if n.isnumeric():
            flag = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            print()
        if flag:
            break
    return int(n)


print('-=' * 30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
