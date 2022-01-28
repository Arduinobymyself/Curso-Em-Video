from random import choice
a1 = input('Nome aluno 1: ')
a2 = input('Nome aluno 2: ')
a3 = input('Nome aluno 3: ')
a4 = input('Nome aluno 4: ')
lista = [a1, a2, a3, a4]
s = choice(lista)
print('O aluno escolhido foi {}'.format(s))
