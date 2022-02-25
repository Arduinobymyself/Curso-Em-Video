'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’)
Saída:
---------------
  Olá, Mundo!
---------------
'''
def mensagem(moldura, texto):
  comp = len(texto)
  print(moldura*(comp + 10))
  print('|    ' + f'{texto}' + '    |')
  print(moldura*(comp+10))
  print()


mensagem('=', 'ABMSTELECOM')
mensagem('~', 'NOTA DOS ALUNOS')
mensagem('*','O CURSO DE PYTHON É MUITO BOM!')
mensagem('-', 'Arduino By MySelf')

