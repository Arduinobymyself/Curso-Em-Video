from random import shuffle
a1 = input('Nome aluno 1: ')
a2 = input('Nome aluno 2: ')
a3 = input('Nome aluno 3: ')
a4 = input('Nome aluno 4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação é: {}'.format(lista))
