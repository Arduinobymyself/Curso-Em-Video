'''
Exercício Python 105: Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
'''

def notas(*notas, sit=False):
  """
  Função para analisar notas e situação de vários alunos
  :param notas: uma ou mais notas dos alunos (aceita várias)
  :param sit: valor opcional, indicando se deve ou não adicionar a situação
  :return: dicionários com as várais notas e a situação
  """

  n = dict()
  n['total'] = len(notas)
  n['maior'] = max(notas)
  n['menor'] = min(notas)
  n['media'] = sum(notas)/len(notas)

  if sit:
    if n['media'] >= 7:
      n['situacao'] = 'BOA'
    elif n['media'] >= 5:
      n['sitacao'] = 'RAZOÁVEL'
    else:
      n['situacao'] = 'RUIM'
  return n


print(notas(9.2, 7.6, 4.6, 8.0, sit=True))
