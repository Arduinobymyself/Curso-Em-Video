'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre o conteúdo
da estrutura na tela.
'''

aluno = dict()

aluno['nome'] = str(input("Qual o nome do aluno: "))
aluno['media'] = float(input(f"Qual é a média do {aluno['nome']}: "))

if aluno['media'] < 5:
  aluno['situacao'] = 'Reprovado'
elif aluno['media'] >= 7:
  aluno['situacao'] = 'Aprovado'
else:
  aluno['situacao'] = 'recuperação'

print('-=' * 30)
for k, v in aluno.items():
  print(f'- {k} = {v}')
print()
