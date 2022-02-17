'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias
pessoas, guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
pessoa = dict()
galera = list()
soma, media = 0, 0

while True:
  pessoa.clear()
  pessoa['nome'] = str(input('Nome: '))
  while True:
    pessoa['sexo'] = str(input('Sexo: [M/F] '))
    if pessoa['sexo'] in 'mMfF':
      break
    print('ERRO! por favor digite apenas M ou F.')
  pessoa['idade'] = int(input('Idade: '))
  soma += pessoa['idade']
  galera.append(pessoa.copy())
  while True:
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'sSnN':
      break
    print('ERRO! Responda apenas S ou N')
  if resp in 'nN':
    break

print('-='*30)
print(galera)
print(f'A - Ao todo temos {len(galera)} pessoas cdastradas.')
media = soma / len(galera)
print(f'B - A média de idade é de {media:5.2f} anos.')
print(f'C - As mulheres cadastradas foram ', end='')
for p in galera:
  if p['sexo'] in 'fF':
    print(f'{p["nome"]} ', end='')
print()
print(f'D - Lista das pessoas que estão acima da média de idade: ', end='')
for p in galera:
  if p['idade'] >= media:
    print('    ')
    for k, v in p.items():
      print(f'{k} = {v}; ', end='')
    print()
print('<< ENCERRADO! >>')









