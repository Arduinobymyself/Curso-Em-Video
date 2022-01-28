# EXERCÍCIO 79

'''
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
'''

lista_num = []

while True:
  n = int(input('Digite um valor: '))
  if n not in lista_num:
    lista_num.append(n)
    print('Valor adicionado com sucesso...')
  else:
    print("Valor duplicado, não será adicionado...")
  resp = input("Quer continuar [S/N] ")
  if resp in 'nN':
    break
print('-='*30)
lista_num.sort()
print(f'Você digitou os valores {lista_num}')