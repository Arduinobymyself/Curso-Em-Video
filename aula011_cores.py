

print('\033[31mOlá Mundo!')
print('\033[31;43mOlá Mundo!\033[m')
print('\033[4;30;45mOlá Mundo!\033[m')
print('\033[7;30mOlá Mundo!\033[m')
print('\033[7;33;47mOlá Mundo!\033[m')
print('\033[4;30;45mOlá Mundo!\033[m')
a = 3
b= 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
nome = 'Marcelo Moraes'
#print('Olá, muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'azul':'\033[34m]',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá, muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))


